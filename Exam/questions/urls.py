from django.urls import path
from . import views
urlpatterns = [
    path('prof/viewexams/',views.view_exams_prof,name="view_exams"),
    path('student/viewexams/',views.view_exams_student,name="view_exams_student"),
]