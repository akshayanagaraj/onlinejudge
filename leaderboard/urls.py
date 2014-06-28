from django.conf.urls import url,patterns
from leaderboard import views

urlpatterns = patterns('',
        url(r'^leaderboard/?$',views.leader)
        )
