
from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^projects/$', views.ProjectListView.as_view(), name='projects'),
    re_path(r'^project/(?P<pk>\d+)$', views.ProjectDetailView.as_view(), name='project-detail'),
    
    re_path(r'^myprojects/$', views.OwnedProjectsByUserListView.as_view(), name='my-projects'),
    re_path(r'^myproject/(?P<pk>\d+)$', views.OwnedProjectsByUserDetailView.as_view(), name='my-project'),
    
    
    re_path(r'^project/create/$', views.ProyectCreate.as_view(), name='proyect-create'),
    re_path(r'^project/(?P<pk>\d+)/update/$', views.ProyectUpdate.as_view(), name='proyect_update'),
    re_path(r'^project/(?P<pk>\d+)/delete/$', views.ProyectDelete.as_view(), name='proyect_delete'),
    
    re_path(r'^myproject/create/$', views.ProyectInstanceCreate.as_view(), name='proyect-i-create'),
    re_path(r'^myproject/(?P<pk>\d+)/update/$', views.ProyectInstanceUpdate.as_view(), name='proyect-i-update'),
    re_path(r'^myproject/(?P<pk>\d+)/delete/$', views.ProyectInstanceDelete.as_view(), name='proyect-i-delete'),

]