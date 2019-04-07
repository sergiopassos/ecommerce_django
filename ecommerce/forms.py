from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

# https://docs.djangoproject.com/en/2.1/ref/forms/widgets/

class ContactForm(forms.Form):
	"""
	Formulário para contato 
	"""
	fullname = forms.CharField(
		widget=forms.TextInput(
			attrs={
				"class": "form-control",
				"placeholder": "Your full name",
				"id": "form_full_name",
				}
				)
		)

	email 	 = forms.EmailField(
		widget=forms.EmailInput(
			attrs={
				"class": "form-control",
				"placeholder": "Your e-mail",
				"required": True,
				}
				)
		)

	content  = forms.CharField(
		widget=forms.Textarea(
			attrs={
				"class": "form-control",
				"placeholder": "Your message",
				}
				)
		)

	# Condição para o campo e-mail, o cleaned_data.get() é o retorno do form do metodo (POST/GET)
	def clean_email(self):
		email = self.cleaned_data.get("email")
		if not "inlog.com" in email:
			raise forms.ValidationError("Email has to be inlog.com")
		return email


class LoginForm(forms.Form):
	username = forms.CharField(widget=forms.TextInput(
			attrs={
				"class": "form-control-sm",
				}
				)
	)
	password = forms.CharField(widget=forms.PasswordInput(
			attrs={
				"class": "form-control-sm",
				}
				)
	)

class RegisterForm(forms.Form):
	username = 	forms.CharField()
	email 	 = 	forms.EmailField()
	password = 	forms.CharField(widget=forms.PasswordInput())
	password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput())

	def clean_username(self):
		username = self.cleaned_data.get('username')
		qs = User.objects.filter(username=username)
		if qs.exists():
			raise forms.ValidationError("Username isi taken")
		return username

	def clean_email(self):
		email = self.cleaned_data.get("email")
		qs = User.objects.filter(email=email)
		if qs.exists():
			raise forms.ValidationError("Email is taken")
		return email

	def clean(self):
		data = self.cleaned_data
		password = self.cleaned_data.get('password')
		password2 = self.cleaned_data.get('password2')
		if password2 != password:
			raise forms.ValidationError("Passwords must match.")
		return data

