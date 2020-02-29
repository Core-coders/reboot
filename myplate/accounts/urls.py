from django.urls import path,include,re_path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('login/',views.login_view, name="login"),
    path('logout/',views.logout_view, name="logout"),
    path('test2/',views.test2_view, name="test2"),
    path('test1/',views.test1_view, name="test1"),
    path('test3/',views.test3_view, name="test3"),
    path('dietplan/',views.dietplan_view, name="dietplan"),
    path('billgen/',views.billgen_view, name="billgen"),
    path('stock/',views.stock_view, name="stock"),
    path('render/',views.render_view, name="render"),
    path('deletion/',views.delete_view,name="delete"),
    path('survey/',views.survey_view,name="survey"),
]