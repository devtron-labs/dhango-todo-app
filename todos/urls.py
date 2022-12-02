from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.list_todo_items ),
    path('insert_todo/', views.insert_todo_item, name='insert_todos_item'), # using this name as a form action in-place of explicitly specifying the route
    path('delete_todo/<int:todo_id>/', views.delete_todo_item, name='delete_todos_item')
]