from django.shortcuts import render, redirect

from blog.forms import PostsForm, CommentForm, CategoriesForm
from .models import Photos, Categories


# Create your views here.

def homepage(request):
    posts = Photos.objects.all()
    categories = Categories.objects.all()

    form = PostsForm()

    comment_form = CommentForm()

    if request.method == 'POST':
        forms = PostsForm(request.POST, request.FILES)
        comment_form = CommentForm(request.POST)
        if forms.is_valid():
            form_post = forms.save(commit=False)
            if request.user.is_authenticated:
                form_post.users = request.user
                form_post.save()

            # validate comment form
            if comment_form.is_valid():
                comment_post = comment_form.save(commit=False)
                if request.user.is_authenticated:
                    comment_post.users = request.user
                    comment_post.photo_id = comment_form.cleaned_data['photo_id']
                    comment_post.save()
                return redirect('homepage')

    context = {
        'posts': posts,
        'categories': categories,
        'form': form,
        'comment_form': comment_form
    }
    return render(request, 'blog/homepage.html', context=context)


def add_posts(request):
    form = PostsForm()
    if request.method == 'POST':
        form = PostsForm(request.POST, request.FILES)
        if form.is_valid():
            form_post = form.save(commit=False)
            if request.user.is_authenticated:
                form_post.users = request.user
                form_post.save()
                return redirect('homepage')
    context = {'form': form}
    return render(request, 'blog/add_posts.html', context=context)


def edit_posts(request, pk: int):
    posts = Photos.objects.get(id=pk)
    form = PostsForm(instance=posts)
    if request.method == 'POST':
        form = PostsForm(request.POST, request.FILES, instance=posts)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    context = {'form': form, 'post_item': posts}
    return render(request, 'blog/edit_posts.html', context=context)


def delete_posts(request, pk: int):
    posts = Photos.objects.get(id=pk)
    if request.method == 'POST':
        posts.delete()
        return redirect('homepage')
    context = {'post_item': posts}
    return render(request, 'blog/post_delete.html', context=context)


def add_categories(request):
    form = CategoriesForm()
    if request.method == 'POST':
        form = CategoriesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    context = {'category_form': form}
    return render(request, 'blog/add_category.html', context=context)


def category_list(request):
    categories = Categories.objects.all()
    context = {'categories': categories}
    return render(request, 'users/show-profile.html', context=context)


def edit_category(request, pk: int):
    category = Categories.objects.get(id=pk)
    form =  CategoriesForm(instance=category)
    if request.method == 'POST':
        form = CategoriesForm(request.POST, request.FILES, instance=category)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    context = {'category_form': form}
    return render(request, 'blog/edit_category.html', context=context)


def delete_category(request, pk: int):
    category = Categories.objects.get(id=pk)
    if request.method == "POST":
        category.delete()
        return redirect('homepage')
    context = {'category_item': category}
    return render(request, 'blog/delete_category.html', context=context)
