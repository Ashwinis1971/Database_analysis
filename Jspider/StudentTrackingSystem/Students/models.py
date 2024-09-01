from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True, default=False)
    education = models.CharField(max_length=100)
    batch = models.CharField(max_length=50)
    
    def __Str__(self):
        return self.name
    
    
class Course(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course_name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    score = models.FloatField()
    
    def __str__(self):
        return f'{self.student.name}: ({self.course_name})'
    
    
class Placement(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100)
    job_role = models.CharField(max_length=100, default=False)
    package = models.FloatField(null=False)
    interview_date = models.DateField(default=0)
    placement_status = models.BooleanField(default=False)
    target_rating = models.FloatField(default=0.0)
    
    def __str__(self):
        return f'{self.student.name} - {self.company_name}'
    
    
    
    
    
    
    
    
    