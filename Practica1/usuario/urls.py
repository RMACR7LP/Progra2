from django.conf.urls import url
from . import views
from usuario import views as usuario_views



urlpatterns = [
   
    url(r'^registro/$', usuario_views.signup_view,name='signup'),
    url(r'^acceso/$', usuario_views.login_view, name='login'),
    url(r'^(?P<username>\w+)/$', usuario_views.perfil_view, name='profile'),
    url(r'^Conf_Perfil/$',usuario_views.edit_perfil,name='edit')
]

