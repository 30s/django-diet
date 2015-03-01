from django.conf.urls import patterns, include, url
from django.views.decorators.csrf import csrf_exempt
from diet import views

urlpatterns = patterns(
    '',
    url(r'^wechat$', csrf_exempt(views.Wechat.as_view()), name="wechat"),
)
