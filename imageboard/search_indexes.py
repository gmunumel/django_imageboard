import datetime
from haystack import indexes
from imageboard.models import Image

class ImageIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)

    def get_model(self):
        return Image

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        qs = self.get_model().objects.all()
        return qs.filter(uploaded_date__lte=datetime.datetime.now())

