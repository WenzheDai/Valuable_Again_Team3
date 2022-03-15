#define the search class
from haystack import indexes
from apps.goods.models import ItemPicture

class ItemsIndex(indexes.SearchIndex, indexes.Indexable):
    # string of retrieval
    # use_template: according items to create the index file. it should put an information to a text.
    text = indexes.CharField(document=True, use_template=True)

    def get_model(self):
        #return my model
        return ItemPicture

    #create the retrieval data.
    def index_queryset(self, using=None):
        return self.get_model().objects.all()