from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'name': "Kofi",
        'age': 23,
        'nationality': 'Ghanaian'
    }
    return(render(request, 'index.html', context))

def counter(request):
    text = request.POST['word']
    number_of_word = len(text.split())
    return(render(request, 'counter.html', {'number': number_of_word}))