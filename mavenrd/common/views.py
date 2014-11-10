from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.core.context_processors import csrf

from cms.helpers import standard_context

from common.helpers import resolve_http_method
from common.forms import UserRegistrationForm, ContactForm

def index(request):
    return render(request, "index.html")

@login_required
def user_profile(request):
    c={"current_user":request.user}
    return render(request, "accounts/profile.html", c)

def register(request):
    new_user_form = UserRegistrationForm()
    c = { "registration_form": new_user_form }
    c.update(csrf(request))

    def get():
        return render(request, 'registration/register.html', c)

    def post():
        new_user_form = UserRegistrationForm(request.POST)
        c.update({ "registration_form": new_user_form })
        if new_user_form.is_valid():
            new_user_form.save()
            return redirect("login")
        
        return render(request, 'registration/register.html', c)

    return resolve_http_method(request, [get, post])

def contact(request):
    c = standard_context()

    def get():
        c.update({'contact_form': ContactForm()})
        return render(request, 'pages/contact.html', c)

    def post():
        contact_form = ContactForm(request.POST)

        if contact_form.is_valid():
            contact_form.send_mail()
            messages.add_message(request, messages.SUCCESS, "Email Sent!")
            return redirect(request.path)

        c.update({'contact_form': contact_form})

        return render(request, 'pages/contact.html', c)

    return resolve_http_method(request, [get, post])

