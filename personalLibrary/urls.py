from django.urls import path
from .views import *

app_name = "personalLibrary"

urlpatterns = [
    path('', home, name="home"),
    # path('bookCollection', bookCollection, name="bookCollection"),
    path('bookCollection', EeListView.as_view(), name="bookCollection"),
    # path('book/add', addNewBook, name="addNewBook"),
    path('book/add', EeCreateView.as_view(), name="addNewBook"),
    path('book/update/(?P<pk>\d+)$', EeUpdateView.as_view(), name="editBook"),
]
