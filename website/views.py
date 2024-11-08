from multiprocessing import AuthenticationError
from pyexpat.errors import messages
from django.shortcuts import redirect, render


def index(request):
    return render(request, 'index.html',{})

def contact(request):
    return render(request, 'contact.html',{})

def about(request):
    return render(request, 'about.html',{})

def doctor(request):
    return render(request, 'doctor.html',{})

def pricing(request):
    return render(request, 'pricing.html',{})

def department(request):
    return render(request, 'department.html',{})

def login(request):
    return render(request, 'login.html',{})

def home(request):
    return render(request, 'index.html')

def loginAdmin(request):
    return render(request, 'loginAdmin.html',{})

def loginEmploy(request):
    return render(request, 'loginEmploy.html',{})

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = AuthenticationError(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')  # Redirect to a different page after login
        else:
            messages.error(request, "Invalid username or password")
    return render(request, 'login.html')

def dashboard(request):
    return render(request, 'dashboard.html',{})

