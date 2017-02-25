from django.conf.urls import include, url

from django.contrib import admin
admin.autodiscover()

import usermgmt.urls
import contact.urls
import hello.views

# Examples:
# url(r'^$', 'gettingstarted.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    url(r'^$', hello.views.index, name='index'),
    url(r'^db', hello.views.db, name='db'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^user/', include(usermgmt.urls)),
    url(r'^contact/', include(contact.urls)),
]
