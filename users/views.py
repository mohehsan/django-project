from django.shortcuts import render, redirect

# Create your views here.

from blog.models import Photos, Categories
from blog.models import Users
from users.forms import UsersForm


def show_profile(request, pk):
    user = Users.objects.get(id=pk)
    categories = Categories.objects.all()
    posts = Photos.objects.filter(users_id=user.id)
    context = {'user': user, 'posts': posts, 'categories': categories}
    return render(request, 'users/show_profile.html', context=context)

def edit_profile(request, pk: int):
    user = Users.objects.get(id=pk)
    form = UsersForm(instance=user)
    if request.method == 'POST':
        form = UsersForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('show_profile')
    context: dict = {'user': user, 'form': form}
    return render(request, 'users/edit_profile.html', context=context)