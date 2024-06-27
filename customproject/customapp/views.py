# from django.shortcuts import render, redirect
# from django.http import HttpResponse
# from django.contrib.auth import login, authenticate, logout
# from django.views import View
# from .forms import CustomUserCreationForm, CustomAuthenticationForm



# class SignupView(View):
#     def get(self, request):
#         form = CustomUserCreationForm()
#         return render(request, 'signup.html', {'form': form})

#     def post(self, request):
#         form = CustomUserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect('home')
#         return render(request, 'signup.html', {'form': form})

# class LoginView(View):
#     def get(self, request):
#         form = CustomAuthenticationForm()
#         return render(request, 'login.html', {'form': form})

#     def post(self, request):
#         form = CustomAuthenticationForm(request.POST, request=request)
#         if form.is_valid():
#             user = form.get_user()
#             login(request, user)
#             return redirect('home')
#         return render(request, 'login.html', {'form': form})

# class LogoutView(View):
#     def get(self, request):
#         logout(request)
#         return redirect('home')


from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CustomUserCreationForm, CustomAuthenticationForm

def home(request):
    return render(request, 'home.html')

def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # login(request, user)
            messages.success(request, 'Sign-up successful! You can now log in.')
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'Login successful!')
            return redirect('home')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('home')
