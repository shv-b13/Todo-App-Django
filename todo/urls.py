from django.conf.urls import url
from . import views

urlpatterns = [
    url('', views.todo, name='todo'),
    url('todo/<int:pk>/', views.todo_detail, name='todo_detail'),
    url('todo/new/', views.todo_new, name='todo_new'),
    url('todo/<int:pk>/edit/', views.todo_edit, name='todo_edit'),
]