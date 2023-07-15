
from django.contrib import admin
from django.urls import path,include
from drf_project import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',views.current_datetime),
    path('api/v1/', include('api.urls')),
]
