from django.shortcuts import render,redirect
from django.contrib import messages
import os, sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from DataLogicLayer.WorkerRepository import *
from DataLogicLayer.TaskRepository import *
from  DataLogicLayer.OpportunityRepository import *
from  DataLogicLayer.PostRepository import *
from time import *
# Create your views here.

def login(request):
    if request.method == 'POST':
        phoneNumber = request.POST["username"]
        password = request.POST["password"]
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
    if request.session.get('userr',0):
        user = request.session['userr']
        if not request.session.get('status',0):
            request.session['status'] = ['начать работу',0]
            # status = 'начать работу'

        opportunities = OpportunityRepository().get_worker_opportunities(user[0])
        printOpportunities = []
        for i in opportunities:
            printOpportunities.append(i[2])
        workerPost = WorkerRepository().Get_Worker_Post(user[0])[0][0]
        postName = PostRepository().GetPostName(workerPost)[0][0]
        workerSalary = PostRepository().GetPostSalary(workerPost)[0][0]
        # print(status)
        if request.method == 'POST' and request.session['status'][0] == 'начать работу':
            timeOfStart = time() // 1
            # status = 'завершить работу'
            request.session['status'] = ['завершить работу',time() // 1]
            # print(status)
        elif request.method == 'POST' and request.session['status'][0] == 'завершить работу':
            timeOfStart = request.session['status'][1]
            timeOfend = time() // 1
            print(timeOfend,timeOfStart)
            workedtime =timeOfend - timeOfStart
            hours=int(workedtime//3600)
            workedtime%=3600
            minutes = int(workedtime//60)
            workedtime%=60
            request.session['status'] = ['начать работу', 0]
            # status = 'начать работу'
            # print(status)
            workertime = str(WorkerRepository().Get_Worked_Time(user[0]))[3:11]
            hours+= int(workertime[0])*10+int(workertime[1])
            minutes+= int(workertime[3])*10+int(workertime[4])
            sec = int(workedtime)+int(workertime[6])*10+int(workertime[7])
            newWorkedTime = ''
            if len(str(hours))==1:
                newWorkedTime='0'+str(hours)+':'
            else:
                newWorkedTime = str(hours)+':'
            if len(str(minutes))==1:
                newWorkedTime = newWorkedTime+'0'+str(minutes)+':'
            else:
                newWorkedTime = newWorkedTime + str(minutes) + ':'
            if len(str(sec))==1:
                newWorkedTime= newWorkedTime + '0'+str(sec)
            else:
                newWorkedTime = newWorkedTime + str(sec)
            print(newWorkedTime)
            WorkerRepository().Update_Worked_Time(user[0],newWorkedTime)
            # data = {"duties": printOpportunities, "post": postName, "salary": workerSalary, "status": status}
            # return render(request, 'Miniproekt/main.html', data)
        data = {"duties": printOpportunities, "post": postName, "salary": workerSalary, "status": request.session['status'][0],'us': request.session['status']}
        return render(request, 'Miniproekt/main.html',data)
    return redirect('login')

def tasks(request):
    # class task:
    #     def __init__(self, desc, dl):
    #         self.desc = desc
    #         self.deadline = dl
    if request.session.get('userr',0):
        # data = {"data":[task('asasasa',132),task('asasasa',132),task('asasasa',132),task('asasasa',132),task('asasasa',132),task('asasasa',132),task('asasasa',132),task('asasasa',132),task('asasasa',132),task('asasasa',132),task('asasasa',132),task('asasasa',132),task('asasasa',132),task('asasasa',132),task('asasasa',132),task('asasasa',132),task('asasasa',132),task('afffffa',132)]}
        data = {"tasks":TaskRepository().tasks_by_worker_id(request.session['userr'][0])}
        return render(request, 'Miniproekt/tasks.html', data)
    return redirect('login')

def team(request):
    if request.session.get('userr',0):
        user = request.session['userr']
        team = WorkerRepository().team_name_and_members_by_worker_id(user[0])
        for x in range(len(team)):
            team[x][-1] = team[x][0]==team[x][-1]
        teamName = team[0][-2]
        data = {
            'teamName': teamName,
            'members': team,
        }
        return render(request, 'Miniproekt/team.html', data)
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

def changePassword(request):
    if request.session.get('userr',0):
        if request.method == "POST":
            old = (request.POST["old"]==request.session['userr'][2])
            new = request.POST['new']
            newAgain = request.POST['newAgain']
            if old and (new == newAgain) and "'" not in new:# and ("'" not in new):
                WorkerRepository().update_worker_password(request.session['userr'][1], new)
                request.session['userr'] = [request.session['userr'][0],request.session['userr'][1],new]
                return redirect('main')
            elif not old:
                messages.info(request, "Неправильный старый пароль!")
                return redirect('changepass')
            elif new != newAgain:
                messages.info(request, "Новые пароли не сходятся!")
                return redirect('changepass')
            else:
                messages.info(request, "Пароль содержит недопустимые символы!")
                return redirect('changepass')
        else:
            return render(request, 'Miniproekt/changePassword.html', {'us':request.session['userr']})
    print('\n\n\n\n\n\n\n\nчто-то не так!')
    return redirect('changepass')