from avakatushka import settings

__author__ = 'ava-katushka'

from django.conf.urls import include, url, patterns
from django.contrib import admin
from blog import views




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


from django.conf import settings
# if settings.DEBUG:
#     urlpatterns += patterns('',
#         url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
#             'document_root': settings.MEDIA_ROOT,
#         }),
#         url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {
#             'document_root': settings.STATIC_ROOT,
#         }),
# )
