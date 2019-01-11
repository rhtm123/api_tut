from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from rest_framework import generics
from course.serializers import CourseSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

from rest_framework.pagination import PageNumberPagination



# Create your views here.
from course.models import *
def api1(request):
	courses = list(Course.objects.all().values())
	return JsonResponse(courses, safe=False)

class CourseList(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = (AllowAny,)
    filter_backends = (DjangoFilterBackend,filters.SearchFilter,)
    filter_fields = ('subject', 'teacher',)
    search_fields = ('name', )
    pagination_class = PageNumberPagination

class CourseDetail(generics.RetrieveAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = (AllowAny,)