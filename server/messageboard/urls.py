from django.conf.urls import url

from .views import topic_list, topic_detail, topic_create, topic_delete


urlpatterns = [
    url(r'^(?P<topic_id>\d+)/$', topic_detail, name='topic-detail'),
    url(r'^topic-create/', topic_create, name='topic-create'),
    url(r'^delete/(?P<topic_id>\d+)/$', topic_delete, name='topic-delete'),
    url(r'', topic_list, name='topic-list'),
]