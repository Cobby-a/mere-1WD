from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'name': "Kofi",
        'age': 23,
        'nationality': 'Ghanaian'
    }
    return(render(request, 'index.html', context))