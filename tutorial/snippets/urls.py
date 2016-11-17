from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views

urlpatterns = [
  url(r'^snippets/$', views.SnippetList.as_view()),
  url(r'^snippets/(?P<pk>[0-9]+)/$', views.SnippetDetail.as_view()),
]

# Allows us URLs like host.com/snippets/1.json (if we want it),
# as well as the more traditional host.com/snippets/1/
urlpatterns = format_suffix_patterns(urlpatterns)
