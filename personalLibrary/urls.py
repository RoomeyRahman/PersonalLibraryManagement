from django.urls import path
from .views import *

app_name = "personalLibrary"

urlpatterns = [
    path('', home, name="home"),
    # path('bookCollection', bookCollection, name="bookCollection"),
    path('bookCollection', EaListView.as_view(), name="bookCollection"),
    # path('book/add', addNewBook, name="addNewBook"),
    path('book/add', EeCreateView.as_view(), name="addNewBook"),
]
