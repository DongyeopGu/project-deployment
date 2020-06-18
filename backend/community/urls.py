from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('pagination/', views.page_index),
    path('create/', views.create),
    path('<int:article_pk>/', views.detail),
    path('<int:article_pk>/update/', views.update),
    path('<int:article_pk>/delete/', views.delete),
    path('<int:article_pk>/comment_create/', views.comment_create),
    path('<int:article_pk>/comment_list/', views.comment_list),    
    path('<int:article_pk>/<int:comment_pk>/comment_update/', views.comment_update),
    path('<int:article_pk>/<int:comment_pk>/comment_delete/', views.comment_delete),

]
