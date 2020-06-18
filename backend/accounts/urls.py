from django.urls import path
from django.contrib.auth.decorators import permission_required
from . import views

urlpatterns = [
    path('<user_name>/', views.profile),
    path("accounts/login/", views.LoginAPI.as_view()),
    path("accounts/signup/", views.RegistrationAPI.as_view()),
    path("accounts/user/", views.UserAPI.as_view()),
    path('accounts/user_list/',views.UserList.as_view()),
    path('accounts/user_list/<user_name>/',views.UserList.as_view()),
    path('accounts/user_list/<user_name>/delete/',views.UserList.as_view()),
]