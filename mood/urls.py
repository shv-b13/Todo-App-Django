from django.urls import path
from . import views
from .views import *



urlpatterns = [
	path('', MoodList.as_view(), name = 'mood_list'),
	path('mood/new/', MoodCreate.as_view(), name = 'mood_new'),
	path('mood/detail/<int:pk>', MoodDetail.as_view(), name = 'mood_detail'),
	path('mood/delete/<int:pk>', MoodDelete.as_view(), name = 'mood_delete'),
	path('mood/edit/<int:pk>', MoodUpdate.as_view(), name = 'mood_edit'),
]