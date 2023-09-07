from django.urls import path

from users import views

urlpatterns = [
    path("signup/", views.signup),
    path("login/", views.login),
    path("logout/", views.logout),
    path("<int:user_id>/", views.profile),
]
