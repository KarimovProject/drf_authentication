
from django.contrib import admin
from django.urls import path,include
from rest_framework.urlpatterns import format_suffix_patterns
from api.views import StudentView



urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/', include('api.urls')),   
    path('auth/', include('rest_framework.urls')),
]

urlpatterns=format_suffix_patterns(urlpatterns, allowed=['json', 'html'])
a=0