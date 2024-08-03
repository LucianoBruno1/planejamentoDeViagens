# users/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

User = get_user_model()

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.email = form.cleaned_data.get('email')
            user.save()
            messages.success(request, 'User created successfully.')
            return redirect('login')  # Redirecionar para a página de login após o registro
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})
