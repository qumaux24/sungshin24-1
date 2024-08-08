from django.shortcuts import render


def c_koreapost(request):
    return render(request, 'koreapost.html')

def c_chinapost(request):
    return render(request, 'chinapost.html')

def c_japanpost(request):
    return render(request, 'japanpost.html')
