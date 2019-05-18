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