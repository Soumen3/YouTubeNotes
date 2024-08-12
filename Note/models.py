from django.db import models

# Create your models here.
class Video_detail(models.Model):
	video_id = models.CharField(max_length=100, unique=True)
	video_title = models.CharField(max_length=1000)
	video_description = models.TextField()
	video_channel = models.CharField(max_length=100)

	def __str__(self):
		return self.video_title
	
class Note(models.Model):
	title = models.CharField(max_length=100, blank=True, default='')
	content = models.TextField( blank=False, default='No content')
	time = models.CharField(max_length=100, blank=True, default='')
	video = models.ForeignKey(Video_detail, related_name='notes', on_delete=models.CASCADE, null=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	owner = models.ForeignKey('auth.User', related_name='notes', on_delete=models.CASCADE)

	def __str__(self):
		return self.title
	
