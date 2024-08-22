from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from .forms import CustomUserCreationForm
from django.contrib import messages
from django.contrib.auth.views import LoginView

User = get_user_model()

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            messages.success(request, 'Usuário criado com sucesso.')
            return redirect('login')  # Redirecionar para a página de login após o registro
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})


def profile(request):
    return render(request, 'profile.html')
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
        else:
            return render(request, 'registration/login.html', {'form': form, 'error': 'Nome de usuário ou senha inválidos'})
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})


class CustomLoginView(LoginView):
    template_name = 'registration/login.html'

    def form_invalid(self, form):
        messages.error(self.request, 'Nome de usuário ou senha inválidos. Tente novamente.')
        return super().form_invalid(form)