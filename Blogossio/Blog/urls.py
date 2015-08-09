from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
                       url(r'^$', 'Blog.views.home', name='home'),
                       url(r'^noticias/', 'Blog.views.noticia', name='noticias'),
                       url(r'^herramientas/', 'Blog.views.herramienta', name='herramientas'),
                       url(r'^contactos/', 'Blog.views.contacto', name='contactos'),
                       url(r'^masinformacion/', 'Blog.views.masinfo', name='masinformacion'),
                       url(r'^ver_post/(?P<id_post>[0-9]+)$', 'Blog.views.ver_post', name='posts'),
                       url(r'^save_message/$', 'Blog.views.save_message', name='save_message'),
                       url(r'^contact/$', 'Blog.views.contact', name='contact'),
                       url(r'^categoria/(?P<categoria>[0-9]+)$', 'Blog.views.categoria', name='categoria'),
                       )
