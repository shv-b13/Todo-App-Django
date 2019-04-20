from django.shortcuts import render
from django.views.generic import ListView, UpdateView, DetailView, CreateView, DeleteView
from django.urls import reverse_lazy
from .models import Mood
from datetime import datetime

# Create your views here.


class MoodList(ListView):
	model = Mood 
	context_object_name = 'moods'

class MoodDetail(DeleteView):
	model = Mood 
	context_object_name = 'mood'
	template_name = 'mood/mood_detail.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		return context

class MoodCreate(CreateView):
	model = Mood 
	fields = ['status', 'data', 'scale', 'exercise']
	template_name = 'mood/mood_new.html'

	def from_valid(self, form):
		fcd = form.cleaned_data
		now = timezone.now()
		Mood.object.create(
				status=fcd['status'],
				exercise=fcd['exercise'],
				scale=['scale'],
				data=['data'],
				)
		
	def get_success_url(self):
		return reverse_lazy('mood_list')

class MoodUpdate(UpdateView):
	model = Mood
	fields = ['status', 'scale', 'exercise']
	success_url = reverse_lazy('mood_list')

class MoodDelete(DeleteView):
	model = Mood
	success_url = reverse_lazy('mood_list')






