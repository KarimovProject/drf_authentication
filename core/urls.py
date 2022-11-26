
from django.contrib import admin
from django.urls import path
from api.views import get_students
urlpatterns = [
    path('admin/', admin.site.urls),
    path('students/', get_students)
]
