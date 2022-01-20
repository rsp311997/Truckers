from django import forms

class RegisterForm(forms.Form):
    FirstName=forms.CharField(max_length=50,min_length=2,strip=True,required=True,label="First Name",help_text="First Name",widget=forms.TextInput({'PlaceHolder':"First Name"}),validators=[])
    LastName=forms.CharField(max_length=50,min_length=2,strip=True,required=True,label="Last Name",help_text="Last Name",widget=forms.TextInput({'PlaceHolder':"Last Name"}),validators=[])
    Email=forms.EmailField(required=True,label="Email",help_text="Email",widget=forms.EmailInput({'PlaceHolder':"Email"}),validators=[])
    Username=forms.CharField(min_length=2,strip=True,label="Username",help_text="Username",widget=forms.TextInput({'PlaceHolder':"Username"}),validators=[])
    Password=forms.CharField(min_length=8,label="Password",help_text="Password",widget=forms.PasswordInput({'PlaceHolder':"Password"}),validators=[])
    CPassword=forms.CharField(min_length=8,label="Confirm Passeord",help_text="Confirm Password",widget=forms.TextInput({'PlaceHolder':"Confirm Password"}),validators=[])


class LoginForm(forms.Form):
    Username=forms.CharField(min_length=2,strip=True,label="Username",help_text="Username",widget=forms.TextInput({'PlaceHolder':"Username"}),validators=[])
    Password=forms.CharField(min_length=8,label="Password",help_text="Password",widget=forms.PasswordInput({'PlaceHolder':"Password"}),validators=[])
