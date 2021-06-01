from .models import *


# ----------------------------------------------Project---Manager__queryset

class MyUserQuerySet(models.QuerySet):
    """ QUERYSET are Connected to a Manager to make specific requests"""



class MyUserManager(models.Manager):
    """ Managers are a way to get specifi data from a Model with the help of a queryset """

    def get_queryset(self):
        return MyUserQuerySet(self.model, using=self._db)

