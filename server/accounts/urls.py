from django.conf.urls import url

from .views import (
    login_view,
    logout_view,
    profile_view,
    registration_view
)


urlpatterns = [
    url(r'^login/$', login_view, name='login'),
    url(r'^logout/$', logout_view, name='logout'),
    url(r'^register/$', registration_view, name='register'),
    url(r'^profile/', profile_view, name='profile')
]
