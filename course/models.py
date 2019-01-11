from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
	name = models.CharField(max_length=100)
	is_published = models.BooleanField(default=False)

	def __str__(self):
		return self.name

class Subject(models.Model):
	category = models.ForeignKey(Category, related_name='cat_subject', on_delete=models.SET_NULL, null=True)
	name = models.CharField(max_length=100)
	is_published = models.BooleanField(default=False)

	def __str__(self):
		return self.name

class Course(models.Model):
	subject = models.ForeignKey(Subject, related_name='sub_course', on_delete=models.SET_NULL, null=True)
	name = models.CharField(max_length=255)
	detail = models.TextField()
	requirement = models.TextField()
	teacher = models.ForeignKey(User, related_name='teacher_course', on_delete=models.SET_NULL, null=True)
	time_required = models.IntegerField()
	pub_date = models.DateField(auto_now_add=True)

	def __str__(self):
		return self.name


