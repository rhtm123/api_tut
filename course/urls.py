from django.urls import path, include
from course import views
from rest_framework.generics import RetrieveAPIView
from course.serializers import CourseSerializer

from course.models import *


urlpatterns = [
    path('api/1', views.api1),
    path('courses/', views.CourseList.as_view(), name='course-list'),
   # path('courses/<int:pk>', views.CourseDetail.as_view()),
    path('courses/<int:pk>', RetrieveAPIView.as_view(queryset=Course.objects.all(), serializer_class=CourseSerializer)),
]