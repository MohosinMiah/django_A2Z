from django.http import HttpResponse

from articals.models import Article

def home_view(request):
    name = "Bangladesh"
    # Get data from database
    artical_obj = Article.objects.get( pk=1 )

    title   = artical_obj.title
    content = artical_obj.content
    # Django Template
    CONTENT = f""" Artical Title : {name}  , and Artical Content : {content} """
    return HttpResponse( CONTENT )