from django.contrib import admin
from .models import Note, Video_detail

# Register your models here.
@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
	list_display = ['id', 'title', 'content', 'time', 'video', 'created_at', 'updated_at', 'owner']
	list_filter = ['created_at', 'updated_at', 'owner']
	search_fields = ['title', 'content', 'video_id', 'video_title', 'video_description', 'video_channel']


@admin.register(Video_detail)
class Video_detailAdmin(admin.ModelAdmin):
	list_display = ['id', 'video_id', 'video_title', 'video_description', 'video_channel']
	search_fields = ['video_id', 'video_title', 'video_description', 'video_channel']