
from django.contrib import admin
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from api.views import StudentView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('students/', StudentView.as_view()),
]

urlpatterns=format_suffix_patterns(urlpatterns, allowed=['json', 'html'])