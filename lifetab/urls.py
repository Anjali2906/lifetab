from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.contrib.auth.views import login
from django.conf.urls.static import static

admin.autodiscover()
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'lifetab.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'lifetab.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^todo/', include('todos.urls', namespace='todo')),
    url(r'^login$', login, name="normallogin"),
    url(r'^journal/', include('journal.urls', namespace='journal')),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url('', include('django.contrib.auth.urls', namespace='auth')),
)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

