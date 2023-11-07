from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
def signupView(request):
    form=UserCreationForm()
    template_name='authapp/register.html'
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect( 'login_url')
    context={'form':form}
    return render(request,template_name,context)

def loginView(request):
    template_name='authapp/login.html'
    context={}
    if request.method=='POST':
        un=request.POST.get('un')
        pw=request.POST.get('pw')
        print('_____________',un,pw )
        user=authenticate(username=un,password=pw)
        print("$$$$$$$$$$$",user)

        if user is not None:
            login(request,user)
            return redirect('addqueans_url')


        
    return render(request,template_name,context)
    
def logoutView(request):
    logout(request)
    return redirect('login_url')
