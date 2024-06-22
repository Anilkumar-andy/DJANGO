from django.urls import path
from .views import *

urlpatterns = [
    path('students_data/', get_student, name='get_students_data'),
    path('student_marks/<student_id>/',see_marks,name='student_marks')
]
