from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),

    # API Routes
    path("tasks", views.create, name="create"),
    # path("tasks/<int:task_id>", views.email, name="email"),
    path("tasks/<str:page>", views.page, name="page"),
    ]