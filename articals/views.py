from django.shortcuts import render

# Create your views here.
from articals.models import Article


def home_view(request):
    # Get data from database
    artical_obj = Article.objects.get( pk=1 )
    articals = Article.objects.all()

    context = {
        'artical_obj': artical_obj,
        'articals' : articals
        }
    return render(request, 'articals/home_view.html',context)


def artical_detail(request, artical_id):
    # Get data from database
    artical_obj = Article.objects.get( pk=artical_id )

    context = {
        'artical_obj': artical_obj,
        }
    return render(request, 'articals/artical_details_view.html',context)


def artical_create(request):
    
    context = {}
    return render(request, 'articals/create.html')


def artical_create_post(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        print(title)
        content = request.POST.get('content')
        Article.objects.create(title=title, content=content)
    return render(request, 'articals/create.html')