from django.shortcuts import render, redirect
from .form import CustomUserCreationForm, CustomeAuthenticationForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from verify_email.email_handler import send_verification_email
from .YT_api import search_videos
import json
# Create your views here.

def user_signup(request):
	context = {}
	if request.user.is_authenticated:
		messages.success(request, 'You are already logged in')
		return redirect('home')
	if request.method == 'POST':
		form = CustomUserCreationForm(request.POST)
		if form.is_valid():
			inavtid_user = send_verification_email(request, form)
			return redirect('verification_message')
		else:
			context['form'] = CustomUserCreationForm()
			messages.error(request, 'Invalid input')

	context['form'] = CustomUserCreationForm()
	return render(request, 'auth/user_signup.html', context)

def user_login(request):
	context = {}
	if request.user.is_authenticated:
		messages.success(request, 'You are already logged in')
		return redirect('home')
	if request.method == 'POST':
		form = CustomeAuthenticationForm(data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.success(request, 'You are logged in successfully')
				return redirect('home')
			else:
				context['form'] = CustomeAuthenticationForm()
				messages.error(request, 'Invalid username or password')	
		else:
			print(form.errors)
			context['form'] = CustomeAuthenticationForm()
			messages.error(request, 'Invalid username or password')		
	else:
		context['form'] = CustomeAuthenticationForm()

	return render(request, 'auth/user_login.html', context)

def user_logout(request):
	logout(request)
	messages.success(request, 'You are logged out successfully')
	return redirect('home')

def verification_message(request):
	return render(request, 'email_verification/verification_msg.html')

def home(request):
	return render(request, 'Note/home.html')

def videos(request):
	if request.method == 'POST':
		query = request.POST.get('query')
		if query:
			data = search_videos(query)
			playlists = [item for item in data['data'] if item['type'] == 'playlist']
			videos = [item for item in data['data'] if item['type'] == 'video']
			context = {
				'videos': videos,
				'playlists': playlists,
				'plsyllist_video': len(playlists)
			}
			return render(request, 'Note/videos.html', context)
	return render(request, 'Note/videos.html')

def playVideo(request, video_id):
	title = request.GET.get('title',  "No title")
	description = request.GET.get('description', "No description")
	channel = request.GET.get('channel', "No channel")
	
	context = {
		'video_id': video_id,
		'title': title,
		'description': description,
		'channel': channel,
	}
	return render(request, 'Note/play_video.html', context)

def notes(request):
	return render(request, 'Note/notes.html')