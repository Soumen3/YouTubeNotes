from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name='home'),
	path('videos/', views.videos, name='videos'),
	path('notes/', views.notes, name='notes'),

	# ===================== User Authentication =====================#
	path('signup/', views.user_signup, name='signup'),
	path('login/', views.user_login, name='login'),
	path('logout/', views.user_logout, name='logout'),
]