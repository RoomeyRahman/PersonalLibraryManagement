from django.shortcuts import render
from django.views.generic import TemplateView,ListView

from .forms import *

from .models import *

from pprint import pprint

# Create your views here.
def home(request):
    return render(request, "personalLibrary/index.html")

def bookCollection(request):
    books = Book.objects.all()
    authors = Author.objects.all()
    myBookCollections = MyBookCollection.objects.all()

    context = {
        "books": books,
        "myBookCollection": myBookCollections,
        "authors": authors
    }

    return render(request, "personalLibrary/myBookCollection.html", context)

def addNewBook(request):
    if request.method == "POST":
        form = request.POST
        myBook = MyBookCollection()
        myBook.book = Book.objects.get(pk=form.get("book"))
        myBook.readStatus = form.get("readStatus")
        myBook.myReview = form.get("myReview")
        myBook.myRating = form.get("myRating")


        myBook.save()

        return  render(request, "personalLibrary/index.html")


    context = {
        "form": MyBookCollectionForm
    }
    return render(request, "personalLibrary/addBook.html", context)

# Class based list view
class EaListView(ListView):
    model = MyBookCollection
    template_name = "personalLibrary/myBookCollection.html"

    def get_context_data(self, **kwargs):
        books = Book.objects.all()
        authors = Author.objects.all()
        myBookCollections = MyBookCollection.objects.all()

        context = {
            "books": books,
            "myBookCollection": myBookCollections,
            "authors": authors
        }

        return context

