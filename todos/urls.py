from django.conf.urls import patterns, include, url
from views import *


urlpatterns = patterns('',
	url(r'^create', TodoCreate.as_view(), name="create"),
	url(r'^edit', TodoUpdate.as_view(), name="edit"),
	url(r'^done', TodoDone.as_view(), name="done"),
	url(r'^today', TodoListToday.as_view(), name="today"),
	url(r'^future', TodoListFuture.as_view(), name="future"),
)