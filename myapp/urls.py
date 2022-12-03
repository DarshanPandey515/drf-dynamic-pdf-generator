from django.urls import path
from myapp.views import *

urlpatterns = [
    path('',HomeView.as_view(),name="index"),
    path('pdf/',PdfGenerate.as_view(),name="pdf"),
    path('employee/',EmployeeList.as_view(),name="employee"),
    path('register/', RegisterAPI.as_view()),
    path('crud/<str:id>/', Crudtask.as_view()),

]