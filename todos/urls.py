from django.urls import path

from todos import views

urlpatterns = [
    path("", views.index),
    path("create/", views.create),
    path("<int:todo_id>", views.detail),
    path("<int:todo_id>/delete/", views.delete),
    path("<int:todo_id>/update/", views.update),
]
