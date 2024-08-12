from django.shortcuts import render, redirect
from .form import CustomUserCreationForm, CustomeAuthenticationForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from verify_email.email_handler import send_verification_email
from .YT_api import search_videos
from .models import Note, Video_detail
from django.http import JsonResponse


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
	context = {
		'active_home': 'active'
	}
	return render(request, 'Note/home.html', context)

def videos(request):
	query = request.GET.get('query')
	context = {
		'active_videos': 'active'
	}
	if query:
		data = search_videos(query)
		playlists = [item for item in data['data'] if item['type'] == 'playlist']
		videos = [item for item in data['data'] if item['type'] == 'video']
		context['videos'] = videos
		context['playlists'] = playlists
		context['plsyllist_video'] = len(playlists)
		context['search'] = query
		return render(request, 'Note/videos.html', context)

	return render(request, 'Note/videos.html', context)

def playVideo(request, video_id):
	if not request.user.is_authenticated:
		messages.error(request, 'You are not authorized to view this page')
		return redirect('videos')
	title = request.GET.get('title',  "No title")
	description = request.GET.get('description', "No description")
	channel = request.GET.get('channel', "No channel")

	if request.method == 'POST':
		note_title = request.POST.get('title')
		content = request.POST.get('note')
		time = request.POST.get('time')

		if Video_detail.objects.filter(video_id=video_id).exists():
			video = Video_detail.objects.get(video_id=video_id)
		else:
			video = Video_detail.objects.create(video_id=video_id, video_title=title, video_description=description, video_channel=channel)

		note = Note.objects.create(title=note_title, content=content, video=video, time=time, owner=request.user)
		note.save()
		messages.success(request, 'Note saved successfully')
		return JsonResponse({
			'title':note_title,
			'content':content,
			'time':time,
			})
	
	context = {
		'video_id': video_id,
		'title': title,
		'description': description,
		'channel': channel,
	}

	# get the notes 
	notes = Note.objects.filter(video__video_id=video_id, owner=request.user)
	context['notes'] = notes
	return render(request, 'Note/play_video.html', context)

def notes(request):
	if not request.user.is_authenticated:
		messages.error(request, 'You are not authorized to view this page')
		return redirect('home')

	context = {
		'active_notes': 'active'
	}
	query = request.GET.get('search')
	if query:
		note_title = Note.objects.filter(title__icontains=query, owner=request.user)
		note_content = Note.objects.filter(content__icontains=query, owner=request.user)
		video_title = Note.objects.filter(video__video_title__icontains=query, owner=request.user)
		notes = note_title.union(note_content, video_title)
		context['notes'] = notes
		context['search'] = query
		return render(request, 'Note/notes.html', context)


	notes = Note.objects.filter(owner=request.user)
	context['notes'] = notes
	return render(request, 'Note/notes.html', context)

def dashboard(request, id, username):
	if not request.user.is_authenticated:
		messages.error(request, 'You are not authorized to view this page')
		return redirect('home')
	
	if request.user.id != id:
		messages.error(request, 'You are not authorized to view this page')
		return redirect('home')
	context = {
		'active_dashboard': 'active'
	}
	return render(request, 'Note/dashboard.html', context)