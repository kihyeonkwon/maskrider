from django.http import HttpResponse
from django.shortcuts import redirect, render

from todos.models import Todo


# Create your views here.
def index(request):
    if request.method == "GET":
        todos = Todo.objects.all()
        context = {
            "todos": todos,
        }
        return render(request, "todos/index.html", context)


def create(request):
    if request.method == "GET":
        return render(request, "todos/create.html")
    elif request.method == "POST":
        # Todo 생성 로직
        title = request.POST["title"]
        content = request.POST["content"]
        Todo.objects.create(title=title, content=content, user=request.user)
        return redirect("/todos/")


def detail(request, todo_id):
    if request.method == "GET":
        todo = Todo.objects.get(id=todo_id)
        context = {
            "todo": todo,
        }
        return render(request, "todos/detail.html", context)


def update(request, todo_id):
    if request.method == "GET":
        todo = Todo.objects.get(id=todo_id)
        context = {
            "todo": todo,
        }
        return render(request, "todos/update.html", context)
    elif request.method == "POST":
        todo = Todo.objects.get(id=todo_id)
        title = request.POST["title"]
        content = request.POST["content"]
        print(request.POST.get("is_completed"))
        is_completed = True if request.POST.get("is_completed") == "on" else False
        todo.title = title
        todo.content = content
        todo.is_completed = is_completed
        todo.save()
        return redirect(f"/todos/{todo.id}")


def delete(request, todo_id):
    if request.method == "POST":
        todo = Todo.objects.get(id=todo_id)
        if request.user == todo.user:
            todo.delete()
            return redirect("/todos/")
        else:
            return HttpResponse("어림도없습니다.")
