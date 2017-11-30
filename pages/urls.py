from django.conf.urls import url  # imports the url function
from . import views                # imports the local views.py file

urlpatterns = [                    # lists the url patterns  registered for this app
  # url(r'^$', views.index, name='index'),
  url(r'^contact$', views.contact, name='contact'),
  url(r'([^/]*)', views.index, name='index'),  # regex of everything but the fwd slash
]
