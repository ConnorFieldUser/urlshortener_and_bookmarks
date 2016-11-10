from django.db import models

from django.contrib.auth.models import User


from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.


class Profile(models.Model):

    user = models.OneToOneField('auth.User')
    created = models.DateTimeField(auto_now_add=True)

    @property
    def bookmarks(self):
        return Bookmark.objects.filter(user=self.user)

    def __str__(self):
        return str(self.user)


@receiver(post_save, sender='auth.User')
def create_user_profile(**kwargs):
    created = kwargs.get('created')
    instance = kwargs.get('instance')
    if created:
        Profile.objects.create(user=instance)


class Bookmark(models.Model):
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=50)
    url = models.URLField(max_length=60)
    newrl = models.URLField(max_length=20)
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User)
    private = models.BooleanField()

    def __str__(self):
        return str(self.title)
