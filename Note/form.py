from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django import forms

tailwindcss = " rounded-lg bg-gray-800 w-full :text-gray-200 dark:bg-gray-700 border border-gray-700 focus:border-blue-500 focus:ring-1 focus:ring-blue-500 focus:outline-none text-sm text-gray-200 py-1 px-2 my-1"

class CustomUserCreationForm(UserCreationForm):
	username = forms.CharField(label="Username",
						  widget=forms.TextInput(attrs={'class': tailwindcss ,'placeholder':'Write here...'}))
	email = forms.EmailField(label="Email address", 
						  widget=forms.EmailInput(attrs={'class': tailwindcss , 'placeholder':'Write here...'}))
	first_name = forms.CharField(label="First name",
						  widget=forms.TextInput(attrs={'class': tailwindcss ,'placeholder':'Write here...'}))
	last_name = forms.CharField(label="Last name",
						  widget=forms.TextInput(attrs={'class': tailwindcss ,'placeholder':'Write here...'}))
	date_of_birth = forms.DateField(
						widget=forms.DateInput(attrs={'type': 'date', 'class':tailwindcss, 'range': '1900-01-01, 2021-12-31'}))
	password1 = forms.CharField(label="Password",
						  widget=forms.PasswordInput(attrs={'class': tailwindcss ,'placeholder':'Write here...'}))	
	password2 = forms.CharField(label="Password confirmation",
						  widget=forms.PasswordInput(attrs={'class': tailwindcss ,'placeholder':'Write here...'}))
	class Meta:
		model = User
		fields = ('username', 'email', 'first_name', 'last_name', 'date_of_birth')


	def clean_email(self):
		email = self.cleaned_data.get('email')
		if User.objects.filter(email=email).exists():
			raise ValidationError("User with this Email address already exists. Or may be the email is not verified yet.")
		return email
	

class CustomeAuthenticationForm(AuthenticationForm):
	username = forms.CharField(label="Username",
						  widget=forms.TextInput(attrs={'class': tailwindcss ,'placeholder':'Write here...'}))
	password = forms.CharField(label="Password",
						  widget=forms.PasswordInput(attrs={'class': tailwindcss ,'placeholder':'Write here...'}))	
	class Meta:
		model = User
		fields = ('username', 'password')