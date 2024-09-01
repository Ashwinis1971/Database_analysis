from django.shortcuts import render
from . models import Student, Placement


# Create your views here.

def student_list(request):
    students = Student.objects.all()
    return render(request, 'students/student_list.html', {'Students': students})

def student_detail(request, student_id):
    student = Student.objects.get(id=student_id)
    courses = Student.course_set.all()
    placements = Student.placement_set.all()
    return render(request, 'students/student_detail.html',
                  {
                      'student': student,
                      'courses': courses,
                      'placements': placements
                  })





