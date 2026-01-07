from django.shortcuts import render , redirect
from .forms import StudentForm
from .models import Student
from django.shortcuts import get_object_or_404



def student_list(request):
    students = Student.objects.all()
    return render(request , 'students/student_list.html', {'students': students})
# Create your views here.
def student_create(request):
    if(request.method =='POST'):
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
        else:
            form = StudentForm()
    
    return render(request , 'students/student_form.html' , {'form' : form})

def student_update(request ,id):
    student = get_object_or_404(Student , id =id)
    if(request.method == 'POST'):
        form =StudentForm(request.POST , instance =student)
        if  form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form =StudentForm(instance =student)
    return render(request , 'students/student_form.html',{form : form})

def student_delete(request ,id):
    student =get_object_or_404(Student ,id=id)
    student.delete()
    return redirect('student_list')