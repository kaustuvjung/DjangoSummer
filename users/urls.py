from django.urls import path
from .views import registeredUser,loginUser, logoutUser
app_name="users"
urlpatterns = [
    path('register/',registeredUser, name="signup"),
    path('Login/',loginUser, name="signin"),
    path('Logout/',logoutUser, name="signin"),
]