from django.views.decorators.csrf import csrf_exempt

__author__ = 'andreasfalley'

from rest_framework.views import APIView, Response
from Mockr.api.serializers import MockrUserSerializer, MocksSerializer, BabyNameSerializer, MockRatingSerializer, \
    FavoriteSerializer
from Mockr.models import MockrUser, Mock, BabyName, MockRating, Favorite
from rest_framework import generics


class ListMocks(generics.ListCreateAPIView):
    queryset = Mock.objects.all()
    serializer_class = MocksSerializer

class ListBabyNames(generics.ListCreateAPIView):
    queryset = BabyName.objects.all()
    serializer_class = BabyNameSerializer

class ListMockrUsers(generics.ListCreateAPIView):
    queryset = MockrUser.objects.all()
    serializer_class = MockrUserSerializer

class ListMockRatings(generics.ListCreateAPIView):
    queryset = MockRating.objects.all()
    serializer_class = MockRatingSerializer

class ListFavorites(generics.ListCreateAPIView):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer




