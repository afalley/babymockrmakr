from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class MockrUser(AbstractUser):
    mockr_username = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    is_Mockr = models.BooleanField(default=False)
    is_facebook = models.BooleanField(default=False)

    def __unicode__(self):
        return self.email

    def get_full_name(self):
        return ' '.join([self.first_name, self.last_name])


class BabyName(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, blank=True)
    middle_name = models.CharField(max_length=50, blank=True)
    rank = models.IntegerField(default=0, blank=True)
    mockr_user = models.ForeignKey(MockrUser, related_name='mkuser')

    def __unicode__(self):
        return ' '.join([self.first_name, self.middle_name, self.last_name])


class Mock(models.Model):
    mock_text = models.CharField(max_length=400)
    brutality = models.IntegerField(blank=True, default=0)
    stupidity = models.IntegerField(blank=True, default=0)
    rhyming = models.BooleanField(default=False)
    funny = models.IntegerField(blank=True, default=0)
    baby_name = models.ForeignKey(BabyName, related_name='babyname')
    mockr_user = models.ForeignKey(MockrUser, related_name='mockruser')

    def __unicode__(self):
        return ' '.join([self.mockr_user.username, " - ", self.mock_text])


class Favorite(models.Model):
    mocks = models.ForeignKey(Mock)
    mockr_user = models.ForeignKey(MockrUser)
    is_favorite = models.BooleanField(default=False)

    def __unicode__(self):
        return self.mocks.mock_text











