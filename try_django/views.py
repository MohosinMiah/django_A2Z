from django.http import HttpResponse

from articals.models import Article
from django.shortcuts import render


def home_view(request):
    # Get data from database
    artical_obj = Article.objects.get( pk=1 )
    articals = Article.objects.all()

    context = {
        'artical_obj': artical_obj,
        'articals' : articals
        }
    return render(request, 'home_view.html',context)