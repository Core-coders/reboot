from django.urls import path,include,re_path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('login/',views.login_view, name="login"),
    path('logout/',views.logout_view, name="logout"),
    path('test/',views.test2_view, name="test"),
    path('test1/',views.test1_view, name="test"),
    path('test2/',views.test3_view, name="test"),
    path('dietplan/',views.dietplan_view, name="dietplan"),
    path('menu/',views.menu_view, name="menu"),
    path('billgen/',views.billgen_view, name="billgen"),
]