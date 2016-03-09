from .views import test, question_detail, new, popular
from django.conf.urls import url


urlpatterns = [
    url(r'^$', new),
    url(r'^login/$', test),
    url(r'^signup/$', test),
    url(r'^question/(?P<question_id>[0-9]+)/$', question_detail),
    url(r'^ask/\w*/ $', test),
    url(r'^popular/$', popular),
    url(r'^new/$', test),
]