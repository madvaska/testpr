from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$',views.dep_list, name='dep_list'),
]