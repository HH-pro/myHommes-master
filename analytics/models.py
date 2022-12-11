from django.db import models

# Create your models here.
from django.conf import settings
from django.db import models
from main.models import User

# Create your models here.



class TagViewManager(models.Manager):
    def add_count(self, user, tag):
        obj, created = self.model.objects.get_or_create(user=user,
            tag=tag)
        obj.count += 1
        obj.save()
        return obj


