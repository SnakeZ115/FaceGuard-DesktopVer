from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

# Create your views here.
def login(request):
    return render(request, 'index.html')

def login_process(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if email == "user@gmail.com" and password == "123":
            return redirect('registros')  # Redirige a la página de inicio después del login
        else:
            # Mostrar un mensaje de error o redirigir a una página de error
            pass
    return render(request, 'index.html')

@login_required
def registros(request):
    return render(request, 'registros.html')
