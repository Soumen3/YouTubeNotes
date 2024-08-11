from django.urls import path, include
from . import views

urlpatterns = [
	path('', views.home, name='home'),
	path('videos/', views.videos, name='videos'),
	path('play-video/<str:video_id>/', views.playVideo, name='play_video'),
	path('notes/', views.notes, name='notes'),


	# ===================== User Authentication =====================#
	path('accounts/signup/', views.user_signup, name='signup'),
	path('accounts/login/', views.user_login, name='login'),
	path('accounts/logout/', views.user_logout, name='logout'),

	# ===================== Email Verification =====================#
	path('verification/', include('verify_email.urls')),
	path('verification/msg/', views.verification_message, name='verification_message'),
]