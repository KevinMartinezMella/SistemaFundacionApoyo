from django.shortcuts import render, redirect
from . models import Colaborador, Aportador, Perfil, Aporte, Notificacion, TipoAporte

# Create your views here.


def login(request):
    if request.method == 'POST':
        rut = request.POST.get('rut')
        password = request.POST.get('password')
        try:
            aportador = Aportador.objects.get(rut = rut, password = password)
        except:
            return redirect('login')
        if not aportador:
            return redirect('login')
        request.session['id'] = aportador.id
        request.session['nombre'] = f'{aportador.nombre} {aportador.apellidoPaterno}'
        return redirect('inicioAportador')
    return render(request, 'login.html')

def registro(request):
    if request.method == 'POST':
        perfil = Perfil.objects.get(id=2)
        rut = request.POST.get('rut')
        nombre = request.POST.get('nombre')
        apellidoPaterno = request.POST.get('apellidoPaterno')
        apellidoMaterno = request.POST.get('apellidoMaterno')
        tarjeta = request.POST.get('tarjeta')
        password = request.POST.get('password')
        aportador = Aportador(
            rut = rut,
            nombre = nombre,
            password = password,
            apellidoPaterno = apellidoPaterno,
            apellidoMaterno = apellidoMaterno,
            numeroTarjeta = tarjeta,
            perfil = perfil
        )
        aportador.save()
        try:
            aportador = Aportador.objects.get(rut = rut, password = password)
        except:
            return redirect('login')
        request.session['id'] = aportador.id
        request.session['nombre'] = f'{aportador.nombre} {aportador.apellidoPaterno}'
        return redirect('inicioAportador')
    return render(request, 'registro.html')

def inicioAportador(request):
    aportador = Aportador.objects.get(id = request.session['id'])
    try:
        notificacion = Notificacion.objects.all().filter(aportador = aportador.id)
    except:
        notificacion = None
    try:
        aportes = Aporte.objects.all().filter(aportador = aportador.id)
    except:
        aportes = None
    context = {
        'aportes':aportes,
        'aportador':aportador,
        'notificacion' : notificacion
    }
    return render(request, 'inicio.html', context)

def modificarAporte(request):
    aportador = Aportador.objects.get(id = request.session['id'])
    try:
        aportes = Aporte.objects.all().filter(aportador = aportador.id)
    except:
        aportes = None
    context = {
        'aportador':aportador
    }
    return render(request, 'modificarAporte.html', context)

def aportar(request):
    if request.method == "POST":
        aportador = Aportador.objects.get(id = request.session['id'])
        tipoAporte = TipoAporte.objects.get(id = request.POST.get('tipo'))
        monto = request.POST.get('monto')
        aporte = Aporte(
            montoAporte = monto,
            aportador = aportador,
            tipo = tipoAporte
        )
        aporte.save()
        notificacion = Notificacion(
            aportador = aportador,
            mensaje = 'Muchas Gracias por tu compromiso con nuestra institución.'
        )
        notificacion.save()
    return redirect('inicioAportador')


def loginColaborador(request):
    return render(request, 'loginColaborador.html')