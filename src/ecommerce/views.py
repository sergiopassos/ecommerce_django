from django.contrib.auth import authenticate, login, get_user_model
from django.http import HttpResponse
from django.shortcuts import render, redirect

# importação do formulario de forms.py
from .forms import ContactForm

def home_page(request):
	print(request.session.get("first_name", "Unknown"))
	# request.session['first_name']
	context = {
		"title": "Hello World",
		"content": "Welcome to the homepage",
	}
	template = "home_page.html"
	if request.user.is_authenticated():
		context["premium_content"] = "YEAHHHHHH"
	return render(request, template, context)

def about_page(request):
	context = {
		"title": "About Page",
		"content": "Welcome to the about page",
	}
	template = "home_page.html"
	return render(request, template, context)

def contact_page(request):
	contact_form = ContactForm(request.POST or None)
	context = {
		"title": "Contact",
		"content": "Welcome to the contact page",
		"form": contact_form,
	}
	if contact_form.is_valid():
		print(contact_form.cleaned_data)
	template = "contact/view.html"
	# if request.method == "POST":
	# 	print(request.POST)
	# 	print(request.POST.get('fullname'))
	# 	print(request.POST.get('email'))
	# 	print(request.POST.get('content'))
	return render(request, template, context)
	