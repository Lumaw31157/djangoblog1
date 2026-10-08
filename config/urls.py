from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
import debug_toolbar

urlpatterns = [
    path("admin/", admin.site.urls),
    path("login/", auth_views.LoginView.as_view(template_name="blog/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(next_page="home"), name="logout"),
    path("", include("blog.urls")),
    path("_debug_/", include(debug_toolbar.urls)),
]
handler403 = "blog.views.custom_403"