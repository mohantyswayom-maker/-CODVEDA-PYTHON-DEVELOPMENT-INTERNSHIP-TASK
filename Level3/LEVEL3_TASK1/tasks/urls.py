from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),

    path('register/', views.register, name='register'),

    path(
        'login/',
        auth_views.LoginView.as_view(
            template_name='login.html'
        ),
        name='login'
    ),

    path(
        'logout/',
        auth_views.LogoutView.as_view(),
        name='logout'
    ),

    path(
        'complete/<int:task_id>/',
        views.complete_task,
        name='complete'
    ),

    path(
        'delete/<int:task_id>/',
        views.delete_task,
        name='delete'
    ),

    path(
        'admin-page/',
        views.admin_page,
        name='admin_page'
    ),

    # password reset
    path(
        'password_reset/',
        auth_views.PasswordResetView.as_view(
            template_name='password_reset.html'
        ),
        name='password_reset'
    ),

    path(
        'password_reset_done/',
        auth_views.PasswordResetDoneView.as_view(
            template_name='password_reset_done.html'
        ),
        name='password_reset_done'
    ),
]