from django.shortcuts import render

# Create your views here.


def index(request):
    context = {"name": "Adu Boat", "age": 24, "Nationality": "Togolese"}
    return render(request, "index.html", context)


def counter(request):
    texts = request.POST["text"]
    number_of_words = len(texts.split())
    return render(request, "counter.html", {"num": number_of_words})
