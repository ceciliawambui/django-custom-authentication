# from django import forms
# from django.contrib.auth.forms import UserCreationForm, UserChangeForm
# from django.contrib.auth import authenticate
# from .models import CustomUser

# class CustomUserCreationForm(UserCreationForm):
#     class Meta:
#         model = CustomUser
#         fields = ('email', 'first_name', 'last_name')

# class CustomUserChangeForm(UserChangeForm):
#     class Meta:
#         model = CustomUser
#         fields = ('email', 'first_name', 'last_name')

# class CustomAuthenticationForm(forms.Form):
#     username = forms.EmailField(label='Email')
#     password = forms.CharField(widget=forms.PasswordInput)

#     def __init__(self, *args, **kwargs):
#         self.request = kwargs.pop('request', None)
#         self.user_cache = None
#         super().__init__(*args, **kwargs)

#     def clean(self):
#         email = self.cleaned_data.get('email')
#         password = self.cleaned_data.get('password')

#         if email and password:
#             self.user_cache = authenticate(self.request, username=email, password=password)
#             if self.user_cache is None:
#                 raise forms.ValidationError("Invalid email or password.")
#             else:
#                 self.confirm_login_allowed(self.user_cache)
#         return self.cleaned_data

#     def confirm_login_allowed(self, user):
#         if not user.is_active:
#             raise forms.ValidationError("This account is inactive.")

#     def get_user(self):
#         return self.user_cache
