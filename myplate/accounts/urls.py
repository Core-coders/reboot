from django.urls import path,include
from . import views

app_name = 'accounts'

urlpatterns = [
    path('login/',views.login_view, name="login"),
    path('test2/',views.test2_view, name="test2"),
    path('logout/',views.logout_view, name="logout"),
]