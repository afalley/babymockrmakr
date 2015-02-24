from django.contrib.auth.tests.test_context_processors import MockUser
from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser, User


# Create your models here.
class MockrUser(models.Model):
    mockr_user = models.ForeignKey(User)
    is_facebook_user = models.BooleanField(default=False)
    is_mockr = models.BooleanField(default=False)

    def __unicode__(self):
        return self.mockr_user.username




# class MockrUser(AbstractBaseUser):
#     mockr_username = models.CharField(max_length=50, blank=True, null=True, unique=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#
#     USERNAME_FIELD = 'mockr_username'
#     is_active = True
#     is_Mockr = models.BooleanField(default=False)
#     is_facebook = models.BooleanField(default=False)
#
#     def __unicode__(self):
#         return self.mockr_username or ''
#
#      def get_full_name(self):
#          return ' '.join([self.first_name, self.last_name])


class BabyName(models.Model):
    name = models.CharField(max_length=50)
    rank = models.IntegerField(default=0, blank=True)
    mockr_user = models.ForeignKey(MockrUser, related_name='mkuser')

    def __unicode__(self):
        return self.name


class Mock(models.Model):
    mock_text = models.CharField(max_length=400)

    rhyming = models.BooleanField(default=False)
    baby_name = models.ForeignKey(BabyName, related_name='babyname')
    mockr_user = models.ForeignKey(MockrUser, related_name='mockruser')
    is_parents_favorite = models.BooleanField(default=False)

    def __unicode__(self):
        return ' '.join([self.mockr_user.username, " - ", self.mock_text])


class Favorite(models.Model):
    mocks = models.ForeignKey(Mock)
    mockr_user = models.ForeignKey(MockrUser)
    is_favorite = models.BooleanField(default=False)

    def __unicode__(self):
        return self.mocks.mock_text


class MockRating(models.Model):
    brutality = models.IntegerField(default=0)
    stupidity = models.IntegerField(default=0)
    funny = models.IntegerField(default=0)
    overall = models.IntegerField(blank=True, default=0)
    mockr_user = models.ForeignKey(MockrUser)
    mock = models.ForeignKey(Mock)












