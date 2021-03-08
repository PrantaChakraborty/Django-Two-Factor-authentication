from django.shortcuts import render
from django.contrib.auth.decorators import login_requeired


# Create your views here.

@login_requeired
def home_view(request):
    return render(request, 'main.html', {})