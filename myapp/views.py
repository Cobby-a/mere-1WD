from django.shortcuts import render
from . import models
# Create your views here.


def index(request):
    feature1 = models.features()
    feature1.id = 1
    feature1.author= 'Adu Boateng'
    feature1.about= 'iuire uufiruoi oiwejoi iewi'
    feature1.pages= 45
    feature1.is_true = True

    feature2 = models.features()
    feature2.id = 2
    feature2.author= 'Cobby Drew'
    feature2.about= "yess we are on what we've been doing the most blud"
    feature2.pages= 56
    feature2.is_true = False

    feature3 = models.features()
    feature3.id = 3
    feature3.author= 'Ankobam Kyere'
    feature3.about= 'kjiue i984 8u9u43 iuhuds ihuei'
    feature3.pages= 34
    feature3.is_true = True

    feature4 = models.features()
    feature4.id = 4
    feature4.author= 'David Cobbina'
    feature4.about= ' 4u 9iri iuire uufiruoi oiwejoi iewi'
    feature4.pages= 23
    feature4.is_true = True

    featuress = [feature1, feature2, feature3, feature4]
    context = {"name": "Adu Boat", "age": 24, "Nationality": "Togolese"}
    return render(request, "index.html", {'feature': featuress})


def counter(request):
    texts = request.POST["text"]
    number_of_words = len(texts.split())
    return render(request, "counter.html", {"num": number_of_words})
