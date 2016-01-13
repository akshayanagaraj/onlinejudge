from django.conf.urls import url,patterns
from users import views

urlpatterns = patterns('',
		url(r'^$',views.home),
		url(r'^register/?$',views.register),
                url(r'^login/?$',views.login_view),
                url(r'^logout/?$',views.logoff),
                url(r'^profile/?$',views.profile),
                url(r'^editprofile/?$',views.edit_profile),
		url(r'^html/?$',views.htmltop)
	)
