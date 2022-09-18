from django.urls import path

from . import views


urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('add-posts/', views.add_posts, name='add_posts'),
    path('edit-posts/<int:pk>', views.edit_posts, name='edit_posts'),
    path('delete-post/<int:pk>', views.delete_posts, name='delete_post'),

    path('add-category/', views.add_categories, name='add_category'),
    path('edit-category/<int:pk>', views.edit_category, name='edit_category'),
    path('delete-category/<int:pk>', views.delete_category, name='delete_category'),
]
