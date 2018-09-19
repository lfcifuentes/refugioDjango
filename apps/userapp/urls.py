from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required
from ..userapp.views import CreatedUser
urlpatterns = [
    url(r'^create', login_required(CreatedUser.as_view()), name="create")
]