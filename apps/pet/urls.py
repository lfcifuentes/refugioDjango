from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required
from ..pet.views import index, pet_view, pet_list, pet_edit, pet_delete, PetList, PetCreate

urlpatterns = [
    url(r'^$', index, name="index"),
    url(r'^new$', login_required(PetCreate.as_view()), name="new"),
    url(r'^list$', login_required(PetList.as_view()), name="list"),
    url(r'^edit/(?P<id>\d+)$', login_required(pet_edit), name="edit"),
    url(r'^delete/(?P<id>\d+)', login_required(pet_delete), name="delete" )
]