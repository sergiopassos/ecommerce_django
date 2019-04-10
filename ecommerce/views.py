from django.contrib.auth import authenticate, login, get_user_model
from django.http import HttpResponse
from django.shortcuts import render, redirect

# importação do formulario de forms.py
from .forms import ContactForm, LoginForm, RegisterForm

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


def login_page(request):
	form = LoginForm(request.POST or None)
	context = {
		"form": form
	}
	print("O usuário está logado? ")
	print(request.user.is_authenticated())
	if form.is_valid():
		print(form.cleaned_data)
		username = form.cleaned_data.get("username")
		password = form.cleaned_data.get("password")
		user = authenticate(request, username=username, password=password)
		print("O usuário está logado? ")
		print(request.user.is_authenticated())		
		if user is not None:
			login(request, user)
			# Redirect to a success page.
			# context['form'] = LoginForm()
			return redirect("/")
		else:
			# Return an 'invalid login' error message.
			return redirect("/login/")
			print("Error")
	template = 'auth/login.html'
	return render(request, template, context)

User = get_user_model()

def register_page(request):
	form = RegisterForm(request.POST or None)
	context = {
		"form": form
	}
	if form.is_valid():
		print(form.cleaned_data)
		username = form.cleaned_data.get("username")
		email = form.cleaned_data.get("email")
		password = form.cleaned_data.get("password")
		new_user = User.objects.create_user(username, email, password)
		print(new_user)
	template = 'auth/register.html'

	return render(request, template, context)