from django.shortcuts import render

# Create your views here.

def main(request):
    class duty:
        def __init__(self, desc):
            self.desc = desc
    data = {"data":[duty('Писать хороший код'), duty("Не писать плохой код"), duty("Не игнорировать беседу проекта")]}
    return render(request, 'Miniproekt/main.html',data)


def tasks(request):
    class task:
        def __init__(self, desc, dl):
            self.desc = desc
            self.deadline = dl
    data = {"data":[task('asasasa',132),task('asasasa',132),task('asasasa',132),task('asasasa',132),task('asasasa',132),task('asasasa',132),task('asasasa',132),task('asasasa',132),task('asasasa',132),task('asasasa',132),task('asasasa',132),task('asasasa',132),task('asasasa',132),task('asasasa',132),task('asasasa',132),task('asasasa',132),task('asasasa',132),task('afffffa',132)]}
    return render(request, 'Miniproekt/tasks.html', data)

def team(request):
    return render(request, 'Miniproekt/team.html', )

def me(request):
    class field:
        def __init__(self, inf):
            self.inf = inf
    data = {"data":[field('Имя'), field('Фамилия'), field('worker@gmail.com'), field('+7(952)356789')]}

    return render(request, 'Miniproekt/me.html', data)