from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
	path('', views.home, name='home'),
	path('videos/', views.videos, name='videos'),
	path('play-video/<str:video_id>/', views.playVideo, name='play_video'),
	path('notes/', views.notes, name='notes'),
	path('edit-note/<int:note_id>/<str:video_id>', views.edit_note, name="edit"),
	path('delete-note/<int:note_id>/', views.delete_note, name='delete_note'),
	path('delete-from-video/<int:note_id>/', views.note_delete_from_play_video, name='delete_from_video'),
	path('dashboard/<int:id>/<str:username>/', views.dashboard, name='dashboard'),

	# ===================== User Authentication =====================#
	path('accounts/signup/', views.user_signup, name='signup'),
	path('accounts/login/', views.user_login, name='login'),
	path('accounts/logout/', views.user_logout, name='logout'),

	# ===================== Email Verification =====================#
	path('verification/', include('verify_email.urls')),
	path('verification/msg/', views.verification_message, name='verification_message'),

	# ===================== Password Change ========================#
	path('password_change/', views.CustomPasswordChangeView.as_view(), name='password_change'),

	# ===================== Password Reset ========================#
	path('password_reset/', views.CustomPasswordResetView.as_view(), name='password_reset'),
    path('reset/<uidb64>/<token>/', views.CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
]