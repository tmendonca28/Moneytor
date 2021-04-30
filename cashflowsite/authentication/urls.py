from .views import RegistrationView
from django.urls import path
from django.views.decorators.csrf import csrf_exempt

urlpatterns = {
    path('register', RegistrationView.as_view(), name="register"),
    path('validate-username', UsernameValidationView.as_view(), name="validate-username")
}