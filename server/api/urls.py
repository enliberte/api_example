from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'Sum(.*)', views.SumAPI, name='Sum'),
    url(r'Diff(.*)', views.DiffAPI, name='Diff')
]