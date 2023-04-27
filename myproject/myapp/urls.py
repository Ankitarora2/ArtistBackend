from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import WorkList, ArtistList, WorkCreate, register

urlpatterns = [
    path('works/', WorkList.as_view(), name='work-list'),
    path('artists/', ArtistList.as_view(), name='artist-list'),
    path('works/create/', WorkCreate.as_view(), name='work-create'),
    path('register/', register, name='client-create'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
