from django.conf.urls import url,patterns
from problems import views

urlpatterns = patterns('',
                       url(r'^problems/?$',views.problems),
                       url(r'^problems/(?P<pid>\w+)/?$',views.problem),
                       url(r'^problems/edit/(?P<pid>\w+)/?$',views.editproblem),
                       url(r'^submit/?$',views.submission),
                       url(r'^submissions/(?P<sid>\d+)/?$',views.submit),
                       url(r'^submissions/?$',views.submissions),
                       url(r'^submissionstatus/(?P<sid>\d+)/?$',views.substatus),
                       )
