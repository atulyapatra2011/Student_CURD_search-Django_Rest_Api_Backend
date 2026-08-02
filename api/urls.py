from django.urls import path
from api.views import *

urlpatterns = [
    path('student/',student,name='student'),
    path('studentlist/<int:id>/',studentList,name='student_list'),
    path("students/", StudentSearchAPI, name="student-search"),
]