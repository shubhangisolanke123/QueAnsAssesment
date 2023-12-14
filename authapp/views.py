from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout

def signupView(request):
    """
    View for user registration/signup.
    """
    form = UserCreationForm()
    template_name = 'authapp/register.html'

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_url')

    context = {'form': form}
    return render(request, template_name, context)

def loginView(request):
    """
    View for user login.
    """
    template_name = 'authapp/login.html'
    context = {}

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('vendor-list-create')

    return render(request, template_name, context)

def logoutView(request):
    """
    View for user logout.
    """
    logout(request)
    return redirect('login_url')
