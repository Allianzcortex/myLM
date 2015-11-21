from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import login,logout

from LM.models import myUser,book
from LM.forms import registrationForm,loginForm,addbookForm

from datetime import datetime
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
	return render(request,'LM/index.html')

def login(request):


def register(request):


def add_book(request):
	
	