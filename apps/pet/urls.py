from django.conf.urls import url, include
from ..pet.views import index, pet_view, pet_list, pet_edit, pet_delete, PetList, PetCreate

urlpatterns = [
    url(r'^$', index, name="index"),
    url(r'^new$', PetCreate.as_view(), name="new"),
    url(r'^list$', PetList.as_view(), name="list"),
    url(r'^edit/(?P<id>\d+)$', pet_edit, name="edit"),
    url(r'^delete/(?P<id>\d+)', pet_delete, name="delete" )
]