from django.shortcuts import render, redirect

# Create your views here.
def main(request):
    return render(request, 'main.html')

def write(request):
    return render(request, 'recipeRegistration.html')

def show(request):
    return render(request, 'recipepage.html')