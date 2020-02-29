from django.urls import path,include,re_path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('login/',views.login_view, name="login"),
    # re_path('login/(?P<slug>[\w-]+)/',views.test2_view,name="details"),
    path('logout/',views.logout_view, name="logout"),
]