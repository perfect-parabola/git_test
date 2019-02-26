from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', main, name = "main"),
    url(r'^create/$', create_post1, name="create_post1"),
    url(r'^create2/$', create_post2, name="create_post2"),
    url(r'^created/$', post_created, name="post_created"),
]