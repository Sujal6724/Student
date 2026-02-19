from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Student, Course
from .forms import StudentForm


# STUDENT LIST with filtering + ordering + pagination
def student_list(request):
	students = Student.objects.all()

	course = request.GET.get('course')
	if course:
		students = students.filter(course__id=course)

	students = students.order_by('name')

	paginator = Paginator(students, 5)
	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)

	courses = Course.objects.all()
	return render(request, 'student_list.html', {'page_obj': page_obj, 'courses': courses})


def student_detail(request, pk):
	student = get_object_or_404(Student, pk=pk)
	return render(request, 'student_detail.html', {'student': student})


# ADD STUDENT (GET + POST)
def add_student(request):
	if request.method == 'POST':
		form = StudentForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('student_list')
	else:
		form = StudentForm()

	return render(request, 'add_student.html', {'form': form})


class CourseListView(ListView):
	model = Course
	template_name = 'course_list.html'


class CourseDetailView(DetailView):
	model = Course
	template_name = 'course_detail.html'


class StudentUpdateView(UpdateView):
	model = Student
	fields = '__all__'
	template_name = 'student_update.html'
	success_url = reverse_lazy('student_list')


class StudentDeleteView(DeleteView):
	model = Student
	template_name = 'student_delete.html'
	success_url = reverse_lazy('student_list')
