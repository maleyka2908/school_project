from django.contrib import admin
from django.urls import path
from students.views import scan_qr, student_list_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('scan/', scan_qr, name='scan_qr'),
    path('students/', student_list_view, name='student_list'),
]