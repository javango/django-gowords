from django.conf.urls.defaults import patterns, url
#
urlpatterns = patterns('gowords.views',
    url(r'^(?P<slug>[-\w]+)/$', 'go', name='goword'),
    
    # ideally this will bring the user to a screen
    # where they can enter or pick a goword
    # url(r'^/$', 'search', name='goword-search'),
)

