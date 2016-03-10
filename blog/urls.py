from avakatushka import settings

__author__ = 'ava-katushka'

from django.conf.urls import include, url, patterns
from django.contrib import admin
from blog import views
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns = [
    url(r'^$', 'blog.views.index', name="index"),
    url(
        r'^/view/(?P<slug>[^\.]+)',
        'blog.views.view_post',
        name='view_blog_post'),
    # url(
    #     r'^/category/(?P<slug>[^\.]+)',
    #     'blog.views.view_category',
    #     name='view_blog_category'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:
    urlpatterns += patterns('',
                            (r'^media/(?P<path>.*)$', 'django.views.static.serve',
                             {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
                            )
