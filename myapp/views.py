from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Feature
from .models import Paragraph
from .utils import get_top_10_paragraphs
from collections import Counter
import heapq
# Create your views here.
def index(request):
    features = Feature.objects.all()
    return render(request, 'index.html', {'features': features})

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']


        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email Already Exist')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username Already Exist')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                return redirect('login')
        else:
            messages.info(request, 'Password incorrect')
            return redirect('register')
    else:
        return render(request, 'register.html')

    

def login(request):
    if request.method == 'POST':
        identifier = request.POST['identifier']
        password = request.POST['password']

        user = auth.authenticate(username=identifier, password=password)
        
        if not user:
            # If not, try getting user by email
            try:
                user_obj = User.objects.get(email=identifier)
                user = auth.authenticate(request, username=user_obj.username, password=password)
            except User.DoesNotExist:
                user = None

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid Credentials! Please try again.')
            return redirect('login')
    else:
        return render(request, 'login.html')
    
def logout(request):
    auth.logout(request)
    return redirect('/')

def counter(request):
    text = request.POST.get('text', '').strip()
    if not text:
        return redirect('/')

    # Split input text into paragraphs
    paragraphs = [p.strip() for p in text.split('\n') if p.strip()]
    
    # Store paragraphs in session for temporary use
    request.session['current_submission'] = paragraphs

    # return redirect('search_word')
    
    return redirect('/')

def search_word_view(request):
    top_paragraphs = []
    search_word = ''
    
    if request.method == 'POST':
        search_word = request.POST.get('search_word', '').strip()
        if search_word:
            # Get paragraphs from the current session (current submission)
            paragraphs = request.session.get('current_submission', [])

            # Apply the search logic
            top_paragraphs = get_top_10_paragraphs(paragraphs, search_word)

    return render(request, 'search.html', {
        'top_paragraphs': top_paragraphs,
        'search_word': search_word
    })


def post(request, pk):
    return render(request, 'post.html', {'pk':pk})