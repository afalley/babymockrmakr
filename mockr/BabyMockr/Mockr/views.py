from django.shortcuts import render
from rest_framework.views import APIView, Response



def home(request):
    return render(request,"index.html")


