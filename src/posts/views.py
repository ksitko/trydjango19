from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def posts_home():
	return HttpResponse("<h1>Hello World</h1>")