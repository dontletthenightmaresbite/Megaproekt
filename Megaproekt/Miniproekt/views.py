from django.shortcuts import render

# Create your views here.

def main(request):
    return render(request, 'Miniproekt/main.html')

def tasks(request):
    class task:
        def __init__(self, desc, dl):
            self.desc = desc
            self.deadline = dl
    data = {"data":[task('aaaaaaaaaaaaaaa aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa',"123"), task('bbbb','234'),]}
    return render(request, 'Miniproekt/tasks.html',context=data)

def team(request):
    return render(request, 'Miniproekt/team.html')

def me(request):
    return render(request, 'Miniproekt/me.html')