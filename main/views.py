from django.shortcuts import render
from .models import Department, Faculty, Student
from .forms import ContactForm

def home(request):
    return render(request, 'main/home.html')

def about(request):
    return render(request, 'main/about.html')

def departments(request):
    departments = Department.objects.all()
    return render(request, 'main/departments.html', {'departments': departments})

def faculty(request):
    faculty = Faculty.objects.all()
    return render(request, 'main/faculty.html', {'faculty': faculty})

def students(request):
    students = Student.objects.all()
    return render(request, 'main/students.html', {'students': students})

def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'main/contact.html', {'form': ContactForm(), 'success': True})
    else:
        form = ContactForm()
    return render(request, 'main/contact.html', {'form': form})
