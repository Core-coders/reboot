from django import forms
from . import models

class CreateArticles(forms.ModelForm):
    class Meta:
        model = models.Billupload
        fields = ['thumb']

class Menu(forms.ModelForm):
    class Meta:
        model = models.Menu
        fields = ['day','dish1','dish2','dish3','dish4']