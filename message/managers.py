from .models import *



------------------------------------Comment---Manager__queryset

class CommentModelQuerySet(models.QuerySet):
    """ QUERYSET are Connected to a Manager to make specific requests"""



class CommentModelManager(models.Manager):
    """ Managers are a way to get specific data from a Model with the help of a queryset """

    def get_queryset(self):
        return CommentModelQuerySet(self.model, using = self._db)
