from django.conf.urls import url,patterns
from problems import views

urlpatterns = patterns('',
                       url(r'^problems/?$',views.problems),
                       url(r'^problems/(?P<pid>\w+)/?$',views.problem),
                       url(r'^submit/?$',views.submission),
                       )
