from django.urls import path

from user import views

urlpatterns = [
    path('signup/', views.registerPage, name="signup"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
]
