from django.shortcuts import render, redirect
from .forms import *


# Homework 1
# 1-misol
def fan_tahrirlash(request, id):
    if request.method == 'POST':
        fan = Fan.objects.get(id=id)
        fan.nomi = request.POST['nomi']
        fan.oqituvchi = Ustoz.objects.get(id=request.POST["oqituvchi"])
        fan.credit = request.POST['credit']
        fan.save()
        return redirect('/fan/')
    context = {
        'fans': Fan.objects.get(id=id),
        'ustozlar': Ustoz.objects.all(),
    }
    return render(request, 'fan_tahrirlash.html', context)

#2-misol
def kurs_tahrirlash(request, id):
    if request.method == 'POST':
        kurs = Kurs.objects.get(id=id)
        kurs.nom = request.POST['nom']
        kurs.daraja = request.POST['daraja']
        kurs.narx = request.POST['narx']
        kurs.chegirma = request.POST['chegirma']
        kurs.save()
        return redirect('/kurs/')
    context = {
        'kurs': Kurs.objects.get(id=id),

    }
    return render(request, 'kurs_tahrirlash.html', context)

# 3-misol
def ustoz_tahrirlash(request, id):
    if request.method == 'POST':
        ustoz = Ustoz.objects.get(id=id)
        ustoz.ism = request.POST['ism']
        ustoz.familiya = request.POST['familiya']
        ustoz.jinsi = request.POST['jinsi']
        ustoz.yosh = request.POST['yosh']
        ustoz.save()
        return redirect('/ustoz/')
    context = {
        'ustoz': Ustoz.objects.get(id=id),

    }
    return render(request, 'ustoz_tahrirlash.html', context)


# Homework 2
# 1-misol
def fans(request):
    if request.method == 'POST':
        data = FanForm(request.POST)
        if data.is_valid():
            data.save()
        return redirect('/fan/')
    context = {
        'fans': Fan.objects.all(),
        'form': FanForm()
    }
    return render(request, 'fan.html', context)



# 2-misol
def kurs(request):
    if request.method == 'POST':
        data = KursForm(request.POST)
        if data.is_valid():
            Kurs.objects.create(
                nom=data.cleaned_data['nom'],
                daraja=data.cleaned_data['daraja'],
                narx=data.cleaned_data['narx'],
                chegirma=data.cleaned_data['chegirma'],
            )
        return redirect('/kurs/')
    context = {
        'kurs': Kurs.objects.all(),
        'form': KursForm()
    }
    return render(request, 'Kurs.html', context)


# 3-misol
def teacher(request):
    if request.method == 'POST':
        data = UstozForm(request.POST)
        if data.is_valid():
            Ustoz.objects.create(
                ism=data.cleaned_data['ism'],
                familiya=data.cleaned_data['familiya'],
                jinsi=data.cleaned_data['jinsi'],
                yosh=data.cleaned_data['yosh'],
            )
        return redirect('/ustoz/')
    context = {
        'teachers': Ustoz.objects.all(),
        'form': UstozForm()
    }
    return render(request, 'ustoz.html', context)
