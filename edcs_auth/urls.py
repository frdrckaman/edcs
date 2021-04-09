from django.urls import path
from .views import LoginView, LogoutView

urlpatterns = [
    path('', LoginView.as_view(redirect_authenticated_user=True), name="login"),
    path('logout/', LogoutView.as_view(template_name="edcs_auth/bootstrap3/login.html"),
         name="logout",),
]
