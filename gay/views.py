from django.shortcuts import render

# Create your views here.
def gayshouse(request):
    return render(request,'main.html')

def log_in(request):
    return render(request,'log_in.html')