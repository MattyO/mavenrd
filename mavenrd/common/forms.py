import django.forms 
from django.contrib.auth.models import User
from django import forms
from django.core.mail import send_mail

class UserRegistrationForm(forms.ModelForm):
    password_confirm = forms.CharField(widget=forms.PasswordInput())
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password', ]
        widgets = { 'password': forms.PasswordInput() }

    def clean(self):
        cleaned_data = super(UserRegistrationForm, self).clean()
        if cleaned_data['password'] != cleaned_data['password_confirm']:
            raise forms.ValidationError("Password and Confirm Password have to be the same")

        return cleaned_data

    def save(self):
        del self.cleaned_data['password_confirm']
        return User.objects.create_user(**self.cleaned_data)

class ContactForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    email = forms.CharField(widget=forms.EmailInput(attrs={"class":"form-control"}))
    message = forms.CharField(widget=forms.Textarea(attrs={"class":"form-control"}))

    def send_mail(self):
        subject = "Contact From MavenRD from {0}".format(self.cleaned_data['name'])
        message = self.cleaned_data['message']
        from_stuf = self.cleaned_data['email']
        me = "odonnell004@gmail.com"

        send_mail(subject, message, from_stuf, (me,) )
