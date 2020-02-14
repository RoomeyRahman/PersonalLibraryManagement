from django.forms import ModelForm, Select

from .models import *

class MyBookCollectionForm(ModelForm):
    class Meta:
        model = MyBookCollection

        fields = ["book", "readStatus", "myRating", "myReview"]

        labels = {
            "book": "Book",
            "readStatus": "Reading Status",
            "myRating": "My Ratings",
            "myReview": "My Review"
        }

        RATING_CHOICES = (
            (1, 'Very Poor'),
            (2, 'Poor'),
            (3, 'Average'),
            (4, 'Good'),
            (5, 'Outstanding'),
        )

        READING_CHOICES = (
            ('read', 'READ'),
            ('currently reading', 'CURRENTLY READING'),
            ('wants to read', 'WANTS TO READ')
        )

        widgets = {
            "book": Select(),
            "readStatus": Select(choices= READING_CHOICES),
            "myRating": Select(choices = RATING_CHOICES),
        }