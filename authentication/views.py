from django.shortcuts import render, HttpResponse

def home(request):
    return render(request, "home/home.html")
def signup(request):
    return render(request, "authentication/singup.html")
def login(request):
    return render(request, "authentication/login.html")
def logout(request):
    return HttpResponse("This is logout")