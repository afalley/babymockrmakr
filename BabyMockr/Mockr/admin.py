from django.contrib import admin
from Mockr.models import MockrUser, BabyName, Mock, Favorite
# Register your models here.

admin.site.register(BabyName)
admin.site.register(Mock)
admin.site.register(Favorite)
admin.site.register(MockrUser)
