from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('StudentList',views.StudentList_f),
    path('StudentDetail',views.StudentDetail_f),
    path('StudentDetailDelete',views.StudentDetailDelete_f),
    path('StudentDetailsInsert',views.StudentDetailsInsert_f),
    path('StudentDetailsUpdate',views.StudentDetailsUpdate_f),
]