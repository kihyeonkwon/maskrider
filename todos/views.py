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


def detail(request):
    pass


def update(request):
    pass


def delete(request):
    pass
