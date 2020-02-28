from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout
from django.http import HttpResponse

def test_view(request):
    return render(request,'accounts/test')

def test2_view(request):
    return render(request,'accounts/test2.html')

def test3_view(request):
    return render(request,'accounts/test3.html')   

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if str(form.get_user()) == 'HO':
                login(request,user)
                return render(request,'accounts/test.html')
            elif str(form.get_user()) == 'HM':
                login(request,user)
                return render(request,'accounts/test2.html')
            elif str(form.get_user()) == 'NF':
                login(request,user)
                #return HttpResponse(user)
                return render(request,'accounts/test3.html')
            else:
                return HttpResponse('better luck next time')
            
    else:
         form = AuthenticationForm()
    return render(request,'accounts/login.html',{'form':form})
    
def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('http://127.0.0.1:8000')