from django.db import models
from django.conf import settings
import os

MEDIA_URL = settings.MEDIA_URL
MEDIA_ROOT = settings.MEDIA_ROOT

# Create your models here.
class Image(models.Model):
    # Name image
    name = models.CharField(max_length=100)
    # Description
    description = models.CharField(max_length=200, null=True)
    # author of the image
    author = models.CharField(max_length=100, null=True)
    # traduction (if any)
    translated_by = models.CharField(max_length=100, null=True)
    # date of the work
    uploaded_date = models.DateTimeField('date published')
    # uploader
    uploaded_by = models.CharField(max_length=100)
    # path_name: path of the image
    path_name = models.CharField(max_length=200)
    # Download link 1 of the collections of images
    download_link1 = models.CharField(max_length=250, null=True)
    # Download link 2 of the collections of images
    download_link2 = models.CharField(max_length=250, null=True)
    # Download link 3 of the collection of images
    download_link3 = models.CharField(max_length=250, null=True)
    # Image height
    #image_height = models.PositiveIntegerField(editable=False, null=True)
    # Image width
    #image_width = models.PositiveIntegerField(editable=False, null=True)
    # The image
    # source: http://stackoverflow.com/questions/19371286/django-admin-image-upload-not-saving-on-database
    file = models.FileField(upload_to=MEDIA_ROOT)
                              #width_field="image_width",height_field="image_height")

    def __unicode__(self):
        return self.file.name

    def find_all_images(self):
        list_files = []
        for files in os.listdir(MEDIA_ROOT + self.path_name):
            list_files.append(self.path_name + "/" + files)
        list_files.sort()
        return list_files

    def tags_per_image(self):
       return ImageTag.objects.filter(image = self.id)

    VALID_IMAGE_EXTENSIONS = [
        ".jpg",
        ".jpeg",
        ".png",
        ".gif",
    ]

    # Source: http://timmyomahony.com/blog/upload-and-validate-image-from-url-in-django/
    def valid_url_extension(url, extension_list=VALID_IMAGE_EXTENSIONS):
        # http://stackoverflow.com/a/10543969/396300
        return any([url.endswith(e) for e in extension_list])

    def image_tag(self):
        return u'<img src="%s" />' % self.file.url

class Tag(models.Model):
    # Nombre del titulo del tag
    title = models.CharField(max_length=100)
    images_per_tag = models.ManyToManyField(Image, through='ImageTag')

    def __unicode__(self):
        return self.title

    def find_tag_image(self):
        return MEDIA_ROOT + self.title + ".png"

class ImageTag(models.Model):
    # Relacion a Image
    image = models.ForeignKey(Image)
    # Relacion a Tag
    tag = models.ForeignKey(Tag)
