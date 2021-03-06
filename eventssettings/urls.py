from django.conf.urls import include, url

from django.contrib import admin
admin.autodiscover()

import eventsapp.views

# Examples:
# url(r'^$', 'gettingstarted.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    url(r'^$', eventsapp.views.index, name='index'),
    url(r'^db', eventsapp.views.db, name='db'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^followGroups', eventsapp.views.follow, name='follow'),
]
