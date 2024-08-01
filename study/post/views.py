from django.shortcuts import render, redirect

# Create your views here.
def list(request):
    return render(request, 'main.html')