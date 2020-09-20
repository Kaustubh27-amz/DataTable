from django.urls import path,include
from . import views
urlpatterns=[
  path('',views.about.as_view(),name='about'),
  path('movie_list/',views.Movies_list.as_view(),name='movie_list'),
  path('movie_create/',views.Movies_create.as_view(),name='Create'),
  path('movie_update/<int:pk>/',views.Movies_update.as_view(),name='update'),
  path('movie_delete/<int:pk>/',views.Movies_delete.as_view(),name='delete'),

]
