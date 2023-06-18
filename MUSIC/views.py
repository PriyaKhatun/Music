from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import MusicFile, AccessRequest

def register(request):
    if request.method == 'POST':
        # Process registration form data and create a new user
        # Redirect to login page or homepage
    else:
        # Render registration form template

def user_login(request):
    if request.method == 'POST':
        # Process login form data and authenticate user
        # Redirect to homepage
    else:
        # Render login form template

def homepage(request):
    user = request.user
    public_files = MusicFile.objects.filter(visibility='public')
    private_files = MusicFile.objects.filter(user=user, visibility='private')
    access_requests = AccessRequest.objects.filter(email=user.email)
    protected_files = [req.music_file for req in access_requests]
    # Render homepage template with relevant files
