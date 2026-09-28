from django.urls import path
from . import views
from .views import PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
    path("", views.home, name="home"),
    path("posts/new/", PostCreateView.as_view(), name="post_create"),
    path("posts/<slug:slug>/edit/", PostUpdateView.as_view(), name="post_update"),
    path("posts/<slug:slug>/delete/", PostDeleteView.as_view(), name="post_delete"),
    path("posts/<slug:slug>/", views.post_detail, name="post_detail"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
]