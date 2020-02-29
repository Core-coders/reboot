from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout
from django.http import HttpResponse
from .models import Hmdetails,Studentdetails



def test2_view(request):
    return render(request,'accounts/test2.html')
  

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            hmdetails = Hmdetails.objects.get(hmid=str(user))
            schooldetails = Studentdetails.objects.get(Schoolid=str(hmdetails.schoolid))
            if str(user) == str(hmdetails):
                login(request,user)
                return render(request,'accounts/test2.html',{'hmdetails':hmdetails,'schooldetails':schooldetails})
                #schooldetail = Studentdetails.objects.raw('select * from accounts_Studentdetails,accounts_Hmdetails where accounts_Studentdetails.Schoolid = accounts_Hmdetails.schoolid')

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
            