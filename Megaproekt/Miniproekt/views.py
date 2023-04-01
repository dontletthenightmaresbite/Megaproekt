from django.shortcuts import render,redirect
from django.contrib import messages
import os, sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from DataLogicLayer.WorkerRepository import *
# Create your views here.

def login(request):
    if request.method == 'POST':
        phoneNumber = request.POST["username"]
        password = request.POST["password"]
        request.session.setdefault('userr','')
        # if True or password=='123456':
        idAndPass = WorkerRepository().worker_password_and_id_by_phone_number(phoneNumber)
        if idAndPass and password == idAndPass[0].Password:
            request.session['userr'] = [idAndPass[0].Id,phoneNumber,password]
            return redirect('main')
        else:
            messages.info(request, "Неправильный номер или пароль!")
            return redirect('login')
    else:
        return render(request, 'Miniproekt/login.html')


def main(request):
    class duty:
        def __init__(self, desc):
            self.desc = desc
    if request.session.get('userr',0):
        data = {"duties":[duty('Писать хороший код'), duty("Не писать плохой код"), duty("Не игнорировать беседу проекта"),duty("Слушать максима")],"post":"Программист","salary":"85000"}
        return render(request, 'Miniproekt/main.html',data)
    return redirect('login')

def tasks(request):
    class task:
        def __init__(self, desc, dl):
            self.desc = desc
            self.deadline = dl
    if request.session.get('userr',0):
        data = {"data":[task('asasasa',132),task('asasasa',132),task('asasasa',132),task('asasasa',132),task('asasasa',132),task('asasasa',132),task('asasasa',132),task('asasasa',132),task('asasasa',132),task('asasasa',132),task('asasasa',132),task('asasasa',132),task('asasasa',132),task('asasasa',132),task('asasasa',132),task('asasasa',132),task('asasasa',132),task('afffffa',132)]}
        return render(request, 'Miniproekt/tasks.html', data)
    return redirect('login')

def team(request):
    if request.session.get('userr',0):
        return render(request, 'Miniproekt/team.html', )
    return redirect('login')

def logout(request):
    del request.session['userr']
    return redirect('login')

def me(request):
    # class field:
    #     def __init__(self, inf):
    #         self.inf = inf
    
    if request.session.get('userr',0):
        data = {'us':request.session.get('userr',-1)}
        return render(request, 'Miniproekt/me.html', data)
    return redirect('login')