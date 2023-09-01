from django.urls import path
from django_chess import views

urlpatterns = [
    path("login/", views.login_view, name="login"),
    path("register/", views.register, name="register"),
    path("logout/", views.logout_view, name="logout"),
    path("<int:game_id>/", views.game_view, name="game"),
]
