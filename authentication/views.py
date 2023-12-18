from django.shortcuts import HttpResponse, redirect, render
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from authentication.models import *

# @login_required(login_url="/login")
def home(request):
        # Get the existing notes from the session
    notes = request.session.get('notes', [])

    if request.method == 'POST':
        # Handle form submission to add a new note
        new_note = request.POST.get('new_note', '')
        notes.append(new_note)

        # Update the session with the new notes
        request.session['notes'] = notes
        return redirect(request.path)
    return render(request, "home/home.html", {'notes': notes})

def fl_session_id(request):
    messages.success(request,"Session cookie cleared successfully")
    request.session.flush()
    return redirect("/")

def signup(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        pass1 = request.POST.get("pass1")
        pass2 = request.POST.get("pass2")
        user_obj = User.objects.filter(username = username)

        if pass1 != pass2:
            messages.error(request, "Passwords dont match")
        else:
            password = pass2
            if User.objects.filter(username = username).exists():
                messages.error(request, "Username already exists")
            else:
                
                if User.objects.filter(email = email).exists():
                    messages.error(request, "Email already taken")
                else:
                    user_obj = User.objects.create(username = username, email=email)
                    user_obj.set_password(password)
                    user_obj.save()
                    messages.success(request, "Account activation email sent.")
    return render(request, "registration/signup.html")

def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password = password)
        if user is not None:
            login(request, user)
            messages.success(request, "Logged in successfully")
            return redirect('/')
        else:
            messages.info(request, "Username or password incorrect")
    return render(request, 'registration/login.html')

@login_required(login_url="/login")
def logoutUser(request):
    logout(request)
    return redirect('/login')
    # return HttpResponse("Logout page")
    
@login_required(login_url="/login")
def ViewProfile(request, username):
    profile = Profile.objects.get(user__username=username)
    context = {"profile":profile}
    return render(request, "profile/ViewProfile.html", context)