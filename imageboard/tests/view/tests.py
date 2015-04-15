from django.core.urlresolvers import reverse
from django.test import TestCase
from django.test import Client
from django.conf import settings
from datetime import datetime

from imageboard.models import Image, Tag, ImageTag

import os

MEDIA_ROOT = settings.MEDIA_ROOT

class ImageboardTestCase(TestCase):
  def setUp(self):
    self.c = Client()
  
    # create image object
    Image.objects.create(
      name = "Images_ajls121",
      description = "Images of mountains",
      author = "me",
      translated_by = "me",
      uploaded_date = datetime.now(),
      uploaded_by = "me",
      path_name = "Images",
      download_link1 = "option1",
      download_link2 = "option2",
      download_link3 = "option3"
    )
    self.image = Image.objects.get(name="Images_ajls121")

    # create tag object
    Tag.objects.create(title="Random")
    self.tag = Tag.objects.get(title="Random")

    # create imagetag object
    ImageTag.objects.create(image=self.image, tag=self.tag)

    # create test directory
    self.path = os.path.join(MEDIA_ROOT, self.image.name)

    # creating directory for testing purposes
    if not os.path.exists(self.path):
      os.makedirs(self.path)

  def tearDown(self):
    # removing directory used for test
    if os.path.exists(self.path):
      os.rmdir(self.path)

  def test_image_index(self):
    response = self.c.get(reverse('imageboard:image_index'))
    self.assertEqual(response.status_code, 200)

  def test_image_details(self):
    response = self.c.get(reverse('imageboard:image_details', args=(self.image.pk,)))
    self.assertEqual(response.status_code, 200)

  def test_image_big_index(self):
    response = self.c.get(reverse('imageboard:image_big_index', args=(self.image.pk,)))
    self.assertEqual(response.status_code, 200)

  def test_image_wo_tags_index(self):
    response = self.c.get(reverse('imageboard:image_wo_tags_index'))
    self.assertEqual(response.status_code, 200)

  def test_image_wo_tags_list(self):

    # bad case
    response = self.c.get(reverse('imageboard:image_wo_tags_list'))
    self.assertEqual(response.status_code, 404)

    # good case
    response = self.c.get(reverse('imageboard:image_wo_tags_list'), HTTP_X_REQUESTED_WITH='XMLHttpRequest')
    self.assertEqual(response.status_code, 200)

  def test_ajax_save_tags(self):
  
    # bad case
    response = self.c.get(reverse('imageboard:ajax_save_tags'))
    self.assertEqual(response.status_code, 404)

    # good case
    response = self.c.get(reverse('imageboard:ajax_save_tags'), 
                          {'idimage': self.image.pk, 'tags': self.tag.title },
                          HTTP_X_REQUESTED_WITH='XMLHttpRequest')
    self.assertEqual(response.status_code, 200)

  def test_image_folders_list(self):
    response = self.c.get(reverse('imageboard:image_folders_list'),HTTP_X_REQUESTED_WITH='XMLHttpRequest')
    self.assertEqual(response.status_code, 200)

