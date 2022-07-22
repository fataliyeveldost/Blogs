from django.shortcuts import redirect, render
from.models import CustomUser
from django.contrib.auth import authenticate,login,logout
from.forms import UserCreationForm,LoginForm
from django.contrib import messages
# Create your views here.

def user_register(request):
    form = UserCreationForm()

    if request.method=='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.first_name = user.first_name.lower()
            user.save()
            login(request, user)
            return redirect("all_blogs")

    context={
        "form": form
    }
    return render(request, "register.html", context)




def user_login(request):
    if request.user.is_authenticated:
        return redirect('all_blogs')
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            user = authenticate(request, username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    messages.success(request, "Daxil oldunuz")
                    return redirect("all_blogs")
                else:
                    messages.info(request, "User silinib")
            else:
                messages.info(request, "Username ve ya password yanlisdir")
    else:
        form = LoginForm()

    context = {
        "form": form
    }

    return render(request, "login_page.html", context)

def user_logout(request):
    logout(request)
    return redirect('index')
