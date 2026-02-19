from django.urls import path
from . import views
from .views import CourseListView, CourseDetailView, StudentUpdateView, StudentDeleteView

urlpatterns = [
    path('', views.student_list, name='student_list'),
    path('student/<int:pk>/', views.student_detail, name='student_detail'),
    path('add/', views.add_student, name='add_student'),

    path('courses/', CourseListView.as_view(), name='course_list'),
    path('course/<int:pk>/', CourseDetailView.as_view(), name='course_detail'),

    path('update/<int:pk>/', StudentUpdateView.as_view(), name='student_update'),
    path('delete/<int:pk>/', StudentDeleteView.as_view(), name='student_delete'),
]
