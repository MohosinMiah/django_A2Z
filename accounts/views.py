from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect

from .forms import NewUserForm


def register_user(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			return redirect("/admin")
	form = NewUserForm()
	return render(request, "accounts/register.html", context={"register_form":form})




# Create your views here.
def login_user(request):
    if request.user.is_authenticated:
        return redirect('/admin/')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return redirect('/admin/')
            ...
        else:
            return render( request, 'accounts/login.html', {} )

    return render( request, 'accounts/login.html', {} )


def logout_user(request):
    logout(request)
    return render( request, 'accounts/login.html')