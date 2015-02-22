from django.contrib import admin
# Register your models here.

from Mockr.models import BabyName, Mock, Favorite, MockRating, MockrUser

admin.site.register(BabyName)
admin.site.register(Mock)
admin.site.register(Favorite)
admin.site.register(MockRating)
admin.site.register(MockrUser)
