from django.contrib import admin
from django.urls import path, include
from tasks import views as task_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tasks.urls')),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', task_views.logout_user, name='logout'),
    path('register/', task_views.register, name='register'),
    path('stats/', task_views.task_stats, name='task_stats'),
]
