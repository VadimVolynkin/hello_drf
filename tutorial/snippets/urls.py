from django.conf.urls import url
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views

urlpatterns = [
    url(r'^snippets/$', views.SnippetList.as_view()),
    url(r'^snippets/(?P<pk>[0-9]+)/$', views.SnippetDetail.as_view()),

    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)






# from django.urls import path
# from rest_framework.urlpatterns import format_suffix_patterns
# from snippets import views


# urlpatterns = [
#     path('snippets/', views.snippet_list),
#     path('snippets/<int:pk>', views.snippet_detail),
# ]

# urlpatterns = format_suffix_patterns(urlpatterns)