from users.models import OjUser

x = OjUser.objects.filter(username='aswinmurugesh94@gmail.com')
for i in x:
    print i.username

