from django.shortcuts import render, redirect
from django.http import HttpRequest
from .models import Todo

# Listing all the todo tasks from our table:
# We'll be returning an HTM template file for that

def list_todo_items(request):

    context = { 'todo_list' : Todo.objects.all()} # we'll have all the inserted todo tasks stored in "todo_list"
    return render(request, 'todos/todo_list.html', context)

# new function for the todo task:
def insert_todo_item(request:HttpRequest):

    # fetching the todo task name from the form:
    # content = request.POST['content']

    # inserting this task in the db: (using ORM)
    todo = Todo(content = request.POST['content'])

    # saving 
    todo.save()

    # redirecting to the specific route
    return redirect('/todos/list/')

# Creating a function for delete operation:
def delete_todo_item(request, todo_id):

    # finding the record to be deleted:
    todo_to_delete = Todo.objects.get(id=todo_id)
    todo_to_delete.delete()

    return redirect('/todos/list/')
