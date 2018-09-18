from django.conf.urls import url
from ..adoption.views import index_adoption, RequestList, RequestCreate, RequestUpdate, RequestDelete

urlpatterns = [
    url(r'^index$', index_adoption, name='index'),
    url(r'^request/list$', RequestList.as_view(), name='request_list'),
    url(r'^request/new$', RequestCreate.as_view(), name='request_new'),
    url(r'^request/edit/(?P<pk>\d+)$', RequestUpdate.as_view(), name='request_edit'),
    url(r'^request/delete/(?P<pk>\d+)$', RequestDelete.as_view(), name='request_delete')
]