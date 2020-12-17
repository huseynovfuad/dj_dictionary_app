from django.shortcuts import render,redirect
from .forms import RegistrationForm,LoginForm
from django.contrib.auth import login,authenticate,logout
from .decorators import authorized_user
# Create your views here.



def registration_view(request):
    context = {}
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST or None)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            current_user = authenticate(username=username, password=password)
            login(request, current_user)
            return redirect('home')
    context['form'] = form
    return render(request,'accounts/register.html',context)



def logout_view(request):
    logout(request)
    return redirect('home')


@authorized_user
def login_view(request):
    context = {}
    next = request.GET.get('next')
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST or None)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            current_user = authenticate(username=username,password=password)

            if current_user:
                login(request,current_user)
                if next:
                    return redirect(next)
                return redirect('home')
    context['form']=form
    return render(request,'accounts/login.html',context)