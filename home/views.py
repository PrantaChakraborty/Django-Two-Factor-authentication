from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login

from codes.forms import CodeForm

from accounts.models import CustomUser

from .utils import send_otp

# Create your views here.

@login_required
def home_view(request):
    return render(request, 'main.html', {})


def auth_view(request):
    form = AuthenticationForm()
    if request.method == "POST":
        uname = request.POST.get("username")
        passw = request.POST.get("password")

        user = authenticate(request, username=uname, password=passw)
        if user is not None:
            request.session['pk'] = user.pk
            return redirect('verify-view')
    return render(request, 'auth.html', {'form': form})


def verify_view(request):
    form = CodeForm(request.POST or None)
    pk = request.session.get('pk')
    print(pk)
    if pk:
        user = CustomUser.objects.get(pk=pk)
        code = user.codes
        code_user = f"{user.username}: {user.codes}"
        if not request.POST:
            send_otp(code_user, user.phone_number)
        if form.is_valid():
            number = form.cleaned_data.get('number')

            if str(code) == number:
                code.save()
                login(request, user)
                return redirect('home')
            else:
                return redirect('login-view')
    return render(request, 'verify.html', {'form': form})




