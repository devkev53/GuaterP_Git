from django.urls import path
from django.contrib.auth import views as auth_views

from .views import Home, Reportes

urlpatterns = [
	 path('', auth_views.LoginView.as_view(template_name="base/login.html"), name='login'),
	 path('logout/', auth_views.LogoutView.as_view(template_name="base/login.html"), name='logout'),
	 path('reportes/', Reportes.as_view(), name='reportes'),
]