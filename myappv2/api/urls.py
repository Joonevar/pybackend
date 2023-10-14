
from django.urls import path
from api.views_dir import v01_index, v02_users

urlpatterns = [
    path('', v01_index.IndexApi().as_view()),
    path('accounts/', v02_users.UsersApi().as_view()),
]
