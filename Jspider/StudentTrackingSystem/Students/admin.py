from django.contrib import admin
from . models import Student, Course, Placement
# Register your models here.

admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Placement)