from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from .forms import CustomUserCreationForm
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm

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

def contact(request):
    return render(request, 'contact.html')

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            # Adicione declarações de depuração
            print("Formulário válido. Dados recebidos:")
            print(f"Nome: {name}")
            print(f"Email: {email}")
            print(f"Mensagem: {message}")

            try:
                # Envia o email
                send_mail(
                    f"Mensagem de {name} - {email}",  # Assunto do email
                    message,  # Corpo da mensagem
                    email,  # Email de origem (remetente)
                    [settings.DEFAULT_FROM_EMAIL],  # Email de destino (destinatário)
                    fail_silently=False,
                )
                print("Email enviado com sucesso.")
                return render(request, 'contact_success.html')  # Renderiza uma página de sucesso
            except Exception as e:
                print(f"Erro ao enviar o email: {e}")
                messages.error(request, 'Houve um erro ao enviar sua mensagem. Tente novamente mais tarde.')
        else:
            print("Formulário inválido.")
            print(form.errors)
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})



def about(request):
    return render(request, 'about.html')
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