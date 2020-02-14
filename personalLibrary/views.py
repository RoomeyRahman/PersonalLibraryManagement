from django.shortcuts import render
from .forms import *

# Create your views here.
def home(request):
    return render(request, "personalLibrary/index.html")

def bookCollection(request):
    return render(request, "personalLibrary/myBookCollection.html")

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