from django.contrib import admin
# Register your models here.
from django.contrib.auth.models import User

from Mockr.models import BabyName, Mock, Favorite, MockRating, MockrUser

admin.site.register(BabyName)
admin.site.register(Mock)
admin.site.register(Favorite)
admin.site.register(MockRating)
admin.site.register(MockrUser)
