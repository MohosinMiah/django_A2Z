from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required

# Create your views here.
from articals.models import Article
from .forms import ArticalForm


def home_view(request):
    # Get data from database
    artical_obj = Article.objects.get( pk=1 )
    articals = Article.objects.all()

    context = {
        'artical_obj': artical_obj,
        'articals' : articals
        }
    return render(request, 'articals/home_view.html')


def artical_detail(request, artical_id):
    # Get data from database
    artical_obj = Article.objects.get( pk=artical_id )

    context = {
        'artical_obj': artical_obj,
        }
    return render(request, 'articals/artical_details_view.html',context)

@login_required(login_url='/accounts/login',redirect_field_name='')
def artical_create(request):
    form = ArticalForm()
    context = { 'form' : form }
    return render(request, 'articals/create.html',context)

@login_required(login_url='/accounts/login',redirect_field_name='')
def artical_create_post(request):
    if request.method == 'POST':
        title = request.POST.get('title').upper()
        print(title)
        content = request.POST.get('content')
        Article.objects.create(title=title, content=content)

        form = ArticalForm()
        context = { 'form' : form }
    return redirect('/articals/artical/create')