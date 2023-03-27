from django.shortcuts import render

# Create your views here.

def main(request):
    return render(request, 'Miniproekt/main.html')

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
    return render(request, 'Miniproekt/me.html')