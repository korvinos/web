from .views import test, question_detail, new, popular, \
    ask_form, answer_form
from django.conf.urls import url


urlpatterns = [
    url(r'^$', new),
    url(r'^login/$', test),
    url(r'^signup/$', test),
    url(r'^question/(?P<question_id>[0-9]+)/$', question_detail),
    url(r'^ask/$', ask_form),
    url(r'^popular/$', popular),
    url(r'^new/$', test),
    url(r'^answer/$', answer_form)
]