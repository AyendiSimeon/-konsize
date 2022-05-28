from django.urls import path, include
from index.views import homeview, PostDetail, CategoryList

urlpatterns = [
    path('', homeview, name='homeview'),
    path('blog/<slug:slug>', PostDetail, name='PostDetail'),
    path('category/<slug:slug>', CategoryList, name='CategoryList'),
]
