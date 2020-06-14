from django.urls import path
from . import views
urlpatterns = [
    path('detail/<int:post_id>', views.detail_post, name='blog-details'),
    path('search/', views.search_post, name='search'),
    path('category/<int:id>', views.category_list, name='category-list')
]