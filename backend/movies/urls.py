from django.urls import path, include
from . import views



urlpatterns = [
    path('<int:movie_id>/', views.detail),
    path('list/', views.movie_list),
    path('<int:movie_id>/reviews/', views.review_list),              # 사용자 리뷰 목록
    path('<int:movie_id>/reviews/create/', views.review_create),            # 사용자 리뷰 작성
    path('<int:movie_id>/reviews/<int:review_id>/', views.review_detail),    # 사용자 리뷰 상세 조회
    path('<int:movie_id>/reviews/<int:review_id>/update/', views.review_update), # 사용자 리뷰 내용 업데이트
    path('<int:movie_id>/reviews/<int:review_id>/delete/', views.review_delete), # 사용자 리뷰 삭제 
    path('<int:movie_id>/like/', views.like),
    path('random/list/', views.random_list),
    path('voted/list/', views.voted_list),
    path('<slug:genre_name>/', views.genre_list),
    path('<slug:genre_name>/all/', views.genre_list_all),
    path('search/<str:search_title>/', views.search_movie),
    path('tmdb/search/', views.search_movies),
    path('tmdb/savedb/', views.save_db),
    path('tmdb/top_rated/', views.top_rated_movies),
    path("recommend/genre/", views.recommend_genre),
]