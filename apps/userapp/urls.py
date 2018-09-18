from django.conf.urls import url, include
from ..userapp.views import CreatedUser
urlpatterns = [
    url(r'^create', CreatedUser.as_view(), name="create")
]