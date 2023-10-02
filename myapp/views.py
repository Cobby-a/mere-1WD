from django.shortcuts import render
from .models import features
# Create your views here.


def index(request):
    featuress = features.objects.all()

    context = {"name": "Adu Boat", "age": 24, "Nationality": "Togolese"}
    return render(request, "index.html", {'feature': featuress})


def counter(request):
    texts = request.POST["text"]
    number_of_words = len(texts.split())
    return render(request, "counter.html", {"num": number_of_words})
