from django.shortcuts import render
from rest_framework import filters
from rest_framework.response import Response
from rest_framework.decorators import api_view

from rest_framework import viewsets

from django.core.paginator import Paginator

from .models import *
from .utils import *


# create a viewset
class AdvocateViewSet(viewsets.ModelViewSet):
	# define queryset
	queryset = Advocate.objects.all()
	  
	# specify serializer to be used
	serializer_class = DeveloperSerializer

	filter_backends = [filters.SearchFilter]
	search_fields = ['name']

class CompaniesViewSet(viewsets.ModelViewSet):
    # define queryset
    queryset = Company.objects.all()
      
    # specify serializer to be used
    serializer_class = CompaniesSerializer

    


class CompViewSet(viewsets.ModelViewSet):
    # define queryset
    queryset = Companies.objects.all()
      
    # specify serializer to be used
    serializer_class = CompSerializer