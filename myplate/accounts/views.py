from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout
from django.http import HttpResponse
from .models import Hmdetails,Studentdetails,Menu
from . import forms


#renders HM page
def test2_view(request):
    return render(request,'accounts/test2.html')

#renders NF page
def test1_view(request):
    return render(request,'accounts/test1.html')

#renders HO page
def test3_view(request):
    return render(request,'accounts/test3.html')

def render_view(request):
    menus = Menu.objects.all()
    # return HttpResponse(menu)
    menu = Menu.objects.filter()
    return render(request,'accounts/rendermenu.html',{'menus':menus})

def dietplan_view(request):
    if request.method == 'POST':
        form = forms.Menu(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return redirect('accounts:dietplan')
    else:
        form = forms.Menu() 
    return render(request,'accounts/dietplan.html',{'form':form})

def billgen_view(request):
     if request.method == 'POST':
        form = forms.CreateArticles(request.POST,request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return redirect('accounts:billgen')
     else:
        form = forms.CreateArticles() 
     return render(request,'accounts/billgen.html',{'form':form})

def stock_view(request):
    return render(request,'accounts/stock.html')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():     #checks if the entered values a valid and can be updated to the db
            user = form.get_user()
            #condition for head master login
            if str(form.get_user()) == 'HM':
                hmdetails = Hmdetails.objects.get(hmid=str(user))
                schooldetails = Studentdetails.objects.filter(Schoolid=str(hmdetails.schoolid))
                if str(user) == str(hmdetails):
                    login(request,user)
                    return render(request,'accounts/test2.html',{'hmdetails':hmdetails,'schooldetails':schooldetails})

            # condition for noon feeding commit login
            elif str(form.get_user()) == 'NF':
                login(request,user)
                return render(request,'accounts/test3.html')
            
            elif str(form.get_user()) == 'HO':
                login(request,user)
                return render(request,'accounts/test3.html')

    else:
        form = AuthenticationForm()
    return render(request,'accounts/login.html',{'form':form})
    
def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('accounts:login')




         # if str(form.get_user()) == 'HO':
            #     login(request,user)
            #     return render(request,'accounts/test2.html',{'hmdetails':hmdetails})
            # elif str(form.get_user()) == 'HM':
            #     login(request,user)
            #     return render(request,'accounts/test2.html',{'hmdetails':hmdetails})
            # elif str(form.get_user()) == 'NF':
            #     login(request,user)
            #     return render(request,'accounts/test2.html',{'hmdetails':hmdetails})
            # else:
            #     return HttpResponse('better luck next time')
            