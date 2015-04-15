from django.test import TestCase
from django.conf import settings
from datetime import datetime

from imageboard.models import Image, Tag

import os

MEDIA_ROOT = settings.MEDIA_ROOT

class ImageTestCase(TestCase):
  def setUp(self):
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
    self.path = os.path.join(MEDIA_ROOT, self.image.name)

    # creating directory for testing purposes
    if not os.path.exists(self.path):
      os.makedirs(self.path)

  def tearDown(self):
    # removing directory used for test
    if os.path.exists(self.path):
      os.rmdir(self.path)

  def test_find_all_images(self):  
    self.assertEqual(self.image.find_all_images(), [])

class TagTestCase(TestCase):
  def setUp(self):
    Image.objects.create(name="Images")
    image = Image.objects.get(name="Images")
    Tag.objects.create(title="Random")

  def test_find_tag_image(self):
    tag = Tag.objects.get(title="Random")
    self.assertEqual(tag.find_tag_image(), MEDIA_ROOT + tag.title + ".png")

