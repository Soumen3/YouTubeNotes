from django.shortcuts import render, redirect
from .form import CustomUserCreationForm, CustomeAuthenticationForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


# Create your views here.

def user_signup(request):
	context = {}
	if request.user.is_authenticated:
		messages.success(request, 'You are already logged in')
		return redirect('home')
	if request.method == 'POST':
		form = CustomUserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('login')
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

def home(request):
	return render(request, 'Note/home.html')

def videos(request):
	return render(request, 'Note/videos.html')

def notes(request):
	return render(request, 'Note/notes.html')