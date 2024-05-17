from django.shortcuts import render, redirect
from .forms import UserForm
from .models import User


def index(request):
    users = User.objects.all()

    context = {
        'users': users
    }
    return render(request, 'user/index.html', context)


def create(request):
    if request.method == 'GET':
        form = UserForm()
        context = {
            'form': form,
        }
        return render(request, 'user/criar.html', context=context)
    elif request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('indexUsuario')


def read(request, user_id):
    user = User.objects.get(pk=user_id)
    form = UserForm(instance=user)
    context = {
        'form': form,
        'user': user
    }
    return render(request, 'user/visualizar.html', context=context)


def update(request, user_id):
    user = User.objects.get(pk=user_id)
    if request.method == 'POST':
        form = UserForm(data=request.POST, instance=user)
        if form.is_valid():
            form.save()
        return redirect('visualizarUsuario', user_id)
    else:
        form = UserForm(instance=user)
        context = {
            'form': form,
            'user': user
        }
        return render(request, 'user/criar.html', context=context)


def delete(request, user_id):
    user = User.objects.get(pk=user_id)
    user.delete()
    return redirect('indexUsuario')
