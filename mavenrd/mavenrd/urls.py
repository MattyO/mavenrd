from django.conf.urls import patterns, include, url
from mavenrd import settings 


from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    #url(r'^$', 'common.views.index', name='index'),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve',
                {'document_root': settings.MEDIA_ROOT}),
    url(r'^upload$', 'cms.views.upload'),
    url(r'^profile$', 'common.views.user_profile', name="user_profile"),
    url(r'^login$', 'django.contrib.auth.views.login',  name='login'),
    url(r'^logout$', 'django.contrib.auth.views.logout', {"next_page": "login"}, name='logout'),
    url(r'^reset-password$','django.contrib.auth.views.password_reset', name='reset-password'),
    url(r'^reset-password-done$','django.contrib.auth.views.password_reset_done', name="password_reset_done"),
    url(r'^password-confim/(?P<uidb64>.+)/(?P<token>.+)/$', 'django.contrib.auth.views.password_reset_confirm',name='password_reset_confirm'),
    url(r'^reset-password-complete', 'django.contrib.auth.views.password_reset_complete', name='password_reset_complete'),
    url(r'^register$','common.views.register', name="register"),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', "cms.views.index", name='index'),
    url(r'^contact$', 'common.views.contact', name="contact"),
    url("^([a-zA-z0-9-_]+)/$", "cms.views.page", name='page'),
    url("^blog/([a-zA-z0-9-_]+)/$", "cms.views.post", name='post'),
    url("^posts/$", "cms.views.posts"),
    url("^post/([a-zA-z0-9-_]+)$", "cms.views.post"),
    url("^media-collection/([0-9]+)$", "cms.views.media_list"),
    url("^media-collection/view/([0-9]+)$", "cms.views.media" ),
)
