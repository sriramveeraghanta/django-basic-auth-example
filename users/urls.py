from django.conf.urls import url
from .views import login_view, register_view, logout_view

urlpatterns = [
    url(r'login/$', login_view),
    url(r'register/$', register_view),
    url(r'logout/$', logout_view),
]
