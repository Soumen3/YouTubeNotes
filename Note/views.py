from django.shortcuts import render

# Create your views here.
def home(request):
	return render(request, 'Note/home.html')


def videos(request):
	return render(request, 'Note/videos.html')

def notes(request):
	return render(request, 'Note/notes.html')