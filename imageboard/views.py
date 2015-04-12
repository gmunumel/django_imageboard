# encoding: utf-8

import os

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.decorators.http import require_POST
from django.shortcuts import render_to_response
from django.http import HttpResponse, Http404
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.views import generic
from django.conf import settings

from jfu.http import upload_receive, UploadResponse, JFUResponse

from imageboard.models import Image, ImageTag, Tag

from math import log


# MEDIA_URL
MEDIA_URL = settings.MEDIA_URL

# Maximun number of images per page
IMAGES_PER_PAGE = 5

def paginator_exe(req, list, case=IMAGES_PER_PAGE):
    # Paginator
    paginator = Paginator(list, case) # Show N post per page

    page = req.GET.get('page')
    try:
        pag_images = paginator.page(page)
    except (PageNotAnInteger, TypeError):
        # If page is not an integer, deliver first page.
        pag_images = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        pag_images = paginator.page(paginator.num_pages)
    return pag_images


############################
# TagCloud created by DBurke
# http://dburke.info/blog/logarithmic-tag-clouds/
#################################
def tagcloud(threshold=0, maxsize=1.75, minsize=.75):
    """usage:
        -threshold: Tag usage less than the threshold is excluded from
            being displayed.  A value of 0 displays all tags.
        -maxsize: max desired CSS font-size in em units
        -minsize: min desired CSS font-size in em units
    Returns a list of dictionaries of the tag, its count and
    calculated font-size.
    """
    counts, taglist, tagcloud = [], [], []
    tags = Tag.objects.all()
    for tag in tags:
        #count = tag.items.count()
        count = ImageTag.objects.filter(tag=tag.id).count()
        count >= threshold and (counts.append(count), taglist.append(tag))
    maxcount = max(counts)
    mincount = min(counts)
    constant = log(maxcount - (mincount - 1))/(maxsize - minsize or 1)
    tagcount = zip(taglist, counts)
    for tag, count in tagcount:
        size = log(count - (mincount - 1))/constant + minsize
        tagcloud.append({'tag': tag, 'count': count, 'size': round(size, 7)})
    return tagcloud

####################
# index
###################
def index(request):
    latest_image_list = Image.objects.all().order_by('uploaded_date')

    # Paginator
    pag_images = paginator_exe(request, latest_image_list)

    # Tagcloud
    tag_cloud = tagcloud()

    template = 'images/index_image.html'
    data = {
        'latest_image_list': pag_images.object_list,
        'paginator_images': pag_images,
        'tagcloud': tag_cloud
    }
    return render_to_response(template, data, context_instance=RequestContext(request))

###################
#  detail
###################
def detail(request, image_id):
    image = Image.objects.get(pk=image_id)

    # Tagcloud
    tag_cloud = tagcloud()

    template = 'images/detail_image.html'
    data = {
        'image': image,
        'tagcloud': tag_cloud
    }
    return render_to_response(template, data, context_instance=RequestContext(request))

###################
#  detail
###################
def ib_large(request, image_id):
    image = Image.objects.get(pk=image_id)

    # Paginator
    pag_images = paginator_exe(request, image.find_all_images(),1)

    template = 'images/ib_large_image.html'
    data = {
        'image': image,
        'pag_image': pag_images
    }
    return render_to_response(template, data, context_instance=RequestContext(request))

####################
#  tags
###################
def tags(request):
    tags = Tag.objects.all().order_by('title')

    # Tagcloud
    tag_cloud = tagcloud()

    template = 'tags/index_tags.html'
    data = {
        'tags': tags,
        'tagcloud': tag_cloud
    }
    return render_to_response(template, data, context_instance=RequestContext(request))

####################
#  detail_tags
###################
def detail_tags(request, tag_id):
    tags = Tag.objects.get(pk = tag_id)
    tags_per_image = tags.images_per_tag.all()

    # Paginator
    pag_images = paginator_exe(request, tags_per_image)

    # Tagcloud
    tag_cloud = tagcloud()

    template = 'tags/detail_tags.html'
    data = {
        'tags': pag_images.object_list,
        'paginator_images': pag_images,
        'query': tags.title,
        'tagcloud': tag_cloud
    }
    return render_to_response(template, data, context_instance=RequestContext(request))

###############################
#  images without tags
#################################
def images_wo_tags(request):
    list_image_wo_tags = []
    all_images = Image.objects.all().count()
    for i in range(1,all_images):
        if ImageTag.objects.filter(image=i) == 0:
            list_image_wo_tags.append(Image.objects.get(pk=i))

    # Paginator
    pag_images = paginator_exe(request, list_image_wo_tags)

    # Tagcloud
    tag_cloud = tagcloud()

    template = 'images/images_wo_tags.html'

    data = {
        'image_wo_tags_list': pag_images.object_list,
        'paginator_images': pag_images,
        'tagcloud': tag_cloud
    }

    return render_to_response(template, data, context_instance=RequestContext(request))

#######################
#  list_tags
#######################
def list_tags(request):
    message = ""
    list_tags = Tag.objects.all()
    for i in list_tags:
        message = message + i.title + "~"
    if not request.is_ajax():
        raise Http404
    return HttpResponse(message)

#######################
#  ajax_save_tags
#######################
def ajax_save_tags(request):
    if request.is_ajax():
        image_id = request.GET.get( 'idimage' )
        tags = request.GET.get( 'tags' )
        tags = tags.split(',')

        list_tags = []
        for i in tags:
            try:
                t = Tag.objects.get(title=i)
            except:
                continue
            list_tags.append(t)

        image_instance = Image.objects.get(pk=image_id)

        for i in list_tags:
            if ImageTag.objects.filter(image=image_id, tag=i.id).count() == 0:
                tag_instance = Tag.objects.get(pk=i.id)
                it = ImageTag(image=image_instance, tag=tag_instance)
                it.save()

        list_tags = Image.objects.get(pk=image_id).tags_per_image()

        template = 'images/list_tags.html'
        data = {
            'tags': list_tags
        }
        return render_to_response(template, data, context_instance = RequestContext(request))
    else:
        raise Http404

#######################
#  to test jfu functionality
#######################
def jfu_test(request):

    template = 'images/jfu_test.html'
    data = {
    }
    return render_to_response(template, data, context_instance=RequestContext(request))

#######################
#  uploaded files
#######################
@require_POST
def upload( request ):

    # The assumption here is that jQuery File Upload
    # has been configured to send files one at a time.
    # If multiple files can be uploaded simulatenously,
    # 'file' may be a list of files.
    file = upload_receive( request )

    instance = Image( file = file )
    instance.save()

    basename = os.path.basename( instance.image.path )

    file_dict = {
        'name' : basename,
        'size' : file.size,

        'url': MEDIA_URL + basename,
        'thumbnailUrl': MEDIA_URL + basename,

        'deleteUrl': reverse('jfu_delete', kwargs = { 'pk': instance.pk }),
        'deleteType': 'POST',
    }

    return UploadResponse( request, file_dict )

#######################
#  delete uploaded files
#######################
@require_POST
def upload_delete( request, pk ):
    success = True
    try:
        instance = Image.objects.get( pk = pk )
        os.unlink( instance.file.path )
        instance.delete()
    except Image.DoesNotExist:
        success = False

    return JFUResponse( request, success )

