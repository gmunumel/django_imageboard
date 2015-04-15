from django.db import models
from django.conf import settings
import os

MEDIA_ROOT = settings.MEDIA_ROOT

# Create your models here.
class Image(models.Model):
    # Name image
    name = models.CharField(max_length=100)
    # Description
    description = models.CharField(max_length=1024, null=True, blank=True)
    # author of the image
    author = models.CharField(max_length=100, null=True, blank=True)
    # traduction (if any)
    translated_by = models.CharField(max_length=100, null=True, blank=True)
    # date of the work
    uploaded_date = models.DateTimeField('date published', null=True, blank=True)
    # uploader
    uploaded_by = models.CharField(max_length=100, null=True, blank=True)
    # path_name: path of the image
    path_name = models.CharField(max_length=200, null=True, blank=True)
    # Download link 1 of the collections of images
    download_link1 = models.CharField(max_length=250, null=True, blank=True)
    # Download link 2 of the collections of images
    download_link2 = models.CharField(max_length=250, null=True, blank=True)
    # Download link 3 of the collection of images
    download_link3 = models.CharField(max_length=250, null=True, blank=True)

    def __unicode__(self):
        return self.name

    def find_all_images(self):
        list_files = []
        for files in os.listdir(os.path.join(MEDIA_ROOT, self.name)):
            list_files.append(self.name + "/" + files)
        list_files.sort()
        return list_files

    def tags_per_image(self):
       return ImageTag.objects.filter(image = self.id)

# source: http://stackoverflow.com/a/11814746/992347
def get_path(instance, filename): 
    path = os.path.join(MEDIA_ROOT, instance.folder)
    if not os.path.exists(path):
      os.makedirs(path)
    return os.path.join(path, filename)

class File(models.Model):
    folder = models.CharField(max_length=255)
    # source: http://stackoverflow.com/questions/19371286/django-admin-image-upload-not-saving-on-database
    file = models.ImageField(upload_to=get_path, null=True, blank=True)

    def __unicode__(self):
        return self.file.path

class Tag(models.Model):
    # Name of the tag
    title = models.CharField(max_length=100)
    images_per_tag = models.ManyToManyField(Image, through='ImageTag')

    def __unicode__(self):
        return self.title

    def find_tag_image(self):
        return MEDIA_ROOT + self.title + ".png"

class ImageTag(models.Model):
    # Relation with Image
    image = models.ForeignKey(Image)
    # Relation with Tag
    tag = models.ForeignKey(Tag)
