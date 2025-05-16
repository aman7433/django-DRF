from django.urls import path
from . import views

urlpatterns = [   
    path('students',views.student_view),
    path('students/<int:pk>',views.student_detail_view),
    path('employee/',views.Employee.as_view()),
    
]