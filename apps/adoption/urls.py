from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from ..adoption.views import index_adoption, RequestList, RequestCreate, RequestUpdate, RequestDelete

urlpatterns = [
    url(r'^index$', login_required(index_adoption), name='index'),
    url(r'^request/list$', login_required(RequestList.as_view()), name='request_list'),
    url(r'^request/new$', login_required(RequestCreate.as_view()), name='request_new'),
    url(r'^request/edit/(?P<pk>\d+)$', login_required(RequestUpdate.as_view()), name='request_edit'),
    url(r'^request/delete/(?P<pk>\d+)$', login_required(RequestDelete.as_view()), name='request_delete')
]