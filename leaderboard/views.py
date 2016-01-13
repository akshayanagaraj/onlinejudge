from django.shortcuts import render
from users.models import OjUser


def leader(request):
    u = OjUser.objects.all().order_by('-points','ex_time','tot_sub')
    i = 1
    for j in u:
        j.rank = i
        j.save()
        i += 1
    return render(request,'leaderboard.html',{'u':u})

# Create your views here.
