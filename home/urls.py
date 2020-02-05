from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name="index"),
    path('blog/', views.blog, name="post-list"),
    path('create/', views.post_create, name="post-create"),
    path('post/<id>/', views.post_detail, name="post-detail"),
    path('post/<id>/update/', views.post_update, name="post-update"),
    path('post/<id>/delete/', views.post_delete, name="post-delete"),
    path('search/', views.search, name="search")
]