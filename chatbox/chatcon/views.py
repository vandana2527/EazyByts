from django.shortcuts import render,redirect , HttpResponse
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .models import User, Message
from .forms import UserForm , MessageForm , RegisterForm
# Create your views here.
def catch_all(request):
    return HttpResponse("Welcome to Chatbox!")
# def register(request):
#     if request.method == 'POST':
#         form = RegisterForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect('chat_room')
#     else:
#         form = RegisterForm()
#         return render(request, 'chatcon/register.html', {'form': form})


from django.contrib.auth.models import User
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # Check if the username is already taken
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already taken.')
            return redirect('register')
        
        # Create the new user
        user = User.objects.create_user(username=username, password=password)
        user.save()

        messages.success(request, 'Registration successful. You can now log in.')
        return redirect('login')

    return render(request, 'chatcon/register.html')

    
    
def login_view(request):
    if request.method == 'POST':
        return render(request , 'chatcon/register.html')
        # Username = request.POST['username']
        # password = request.POST['password']
        # user = User.objects.get(username=Username)
        # if user and user.password == password:
        #     login(request, user)
        #     return redirect('chat_room')
    return render(request, 'chatcon/chat_room.html')

@login_required
def chat_room (request):
    messages = Message.objects.filter(room='general').order_by('-timestamp')
    return render(request, 'chat_room.html', {'messages': messages})

@login_required
def send_message(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user
            message.save()
            return redirect('chat_room')
    else:
        form = MessageForm()
        return render(request, 'send_message.html', {'form': form})
