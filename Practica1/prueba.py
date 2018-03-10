import pickle


th= open("usuario/urls.py",'a')
url_pattern="urlpatterns.append('url(r'^acceso/$', usuario_views.login_view, name='login',"
pickle.dump(url_pattern,th,url_patterns)
th.close()
    


