from django.shortcuts import render
from rest_framework import (viewsets, views)

# Create your views here.

class Index(views.View):
    def get(self, request):
        return render(request, 'index.html')
