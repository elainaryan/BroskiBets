from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from picks.models import ScottPick, KanePick
from .forms import ContactForm

def home(request):
    # Render the HTML template home.html
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def vip(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(name, message, from_email, ["broskibets@gmail.com"])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request, "go-vip.html", {'form': form})

def success_view(request):
    return HttpResponse('Success! Thank you for your message.')