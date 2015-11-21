from django import forms
from LM.models import *


class registrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = myUser
        exclude = ('permission',)


class loginForm(form.ModelForm):
	mail = forms.MailField()
	password = forms.CharField(widget=forms.PasswordInput())


class addbookForm(form.ModelForm):
	class Meta:
		model = Book
		fields = '__all__'


# class userprofileForm(form.ModelForm):

