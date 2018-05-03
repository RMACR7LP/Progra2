from django.conf.urls import url
from . import views
from usuario import views as usuario_views 



urlpatterns = [
    url(r'^display/',usuario_views.display_texto_view, name='display'),
    url(r'^subir/', usuario_views.subir_texto_view, name='subir'),
    url(r'^textos/$', usuario_views.textos_view,name='textos'),
    url(r'^registro/$', usuario_views.signup_view,name='signup'),
    url(r'^acceso/$', usuario_views.login_view, name='login'),
    url(r'^(?P<username>\w+)/$', usuario_views.perfil_view, name='profile'),
    
]

