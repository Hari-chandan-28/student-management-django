from django.shortcuts import render , redirect
from .forms import StudentForm
from .models import Student
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate

def signup(request):
    if(request.method == 'POST'):
        form = UserCreationForm(request.POST)
        if(form.is_valid()):
            user = form.save()
            login(request,user)
            return redirect('student_list')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html',{
        'form': form
    })

@login_required
def student_list(request):
    students = Student.objects.all()
    return render(request , 'students/student_list.html', {'students': students})
# Create your views here.
@login_required
def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()

    return render(request, 'students/student_form.html', {'form': form})

@login_required
def student_update(request, id):
    student = get_object_or_404(Student, id=id)
    form = StudentForm(instance=student)

    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')

    return render(
        request,
        'students/student_form.html',
        {'form': form, 'is_edit': True}
    )
@login_required
def student_delete(request ,id):
    student =get_object_or_404(Student ,id=id)
    student.delete()
    return redirect('student_list')
