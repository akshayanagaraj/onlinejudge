from users.models import OjUser

x = OjUser.objects.filter(username='aswinmurugesh94@gmail.com')
print x.username

