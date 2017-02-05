from django.conf.urls import url, include
from web_app import views


urlpatterns = [
    url(r'^categories/$', views.categories_list),
    url(r'^categories/(?P<pk>[0-9]+)/$', views.category_detail),
    url(r'^items/$', views.items_list),
    url(r'^items/(?P<pk>[0-9]+)/$', views.item_detail),
]

