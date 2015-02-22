from django.views.decorators.csrf import csrf_exempt

__author__ = 'andreasfalley'

from rest_framework.views import APIView, Response
from Mockr.api.serializers import MockrUserSerializer, MocksSerializer, BabyNameSerializer
from Mockr.models import MockrUser, Mock
from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework import generics






class ListMockrUsers(APIView):
    def get(self, request, format=None):

        users = MockrUser.objects.all()
        serializer = MockrUserSerializer(users, many=True)

        return Response(serializer.data)


class ListMocks(generics.ListCreateAPIView):
    queryset = Mock.objects.all()
    serializer_class = MocksSerializer




