from django.conf.urls import patterns, include, url
from django.contrib import admin

from Mockr.api.views import ListMockrUsers, ListMocks, ListBabyNames, ListMockRatings, ListFavorites

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'Mockr.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^MockrUser/', ListMockrUsers.as_view()),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^Mocks/', ListMocks().as_view()),
    url(r'^BabyName', ListBabyNames.as_view()),
    url(r'^MockRatings', ListMockRatings.as_view()),
    url(r'^ListFavorites',ListFavorites.as_view()),

)
