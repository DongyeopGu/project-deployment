import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import LoginView from '../views/accounts/LoginView.vue'
import SignupView from '../views/accounts/SignupView.vue'
import UserProfileView from '../views/accounts/UserProfileView.vue'
import ArticleListView from '../views/community/ArticleListView.vue'
import ArticleCreateView from '../views/community/ArticleCreateView.vue'
import ArticleDetailView from '../views/community/ArticleDetailView.vue'
import ArticleUpdateView from '../views/community/ArticleUpdateView.vue'
import MoviesView from '../views/movies/MoviesView.vue'
import MovieReviewsView from '../views/movies/MovieReviewsView.vue'
import MovieDetailView from '../views/movies/MovieDetailView.vue'
import MovieReviewDetailView from '../views/movies/MovieReviewDetailView.vue'
import MovieReviewCreate from '../views/movies/MovieReviewCreate.vue'
import MovieReviewUpdateView from '../views/movies/MovieReviewUpdateView.vue'
import MovieSearchView from '../views/movies/MovieSearchView.vue'
import AdminView from '../views/admin/AdminView.vue'
import GenreAllMovies from '../views/movies/GenreAllMovies.vue'

Vue.use(VueRouter)

  const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/admin',
    name: 'AdminView',
    component: AdminView
  },
  {
    path: '/login',
    name: 'LoginView',
    component: LoginView,
    props: true
  },
  {
    path: '/signup',
    name: 'SignupView',
    component: SignupView
  },
  {
    path: '/user/:name',
    name: 'UserProfileView',
    component: UserProfileView,
    props: route => ({name: String(route.params.name)})
  },
  {
    path: '/community',
    name: 'ArticleListView',
    component: ArticleListView
  },
  {
    path: '/community/post',
    name: 'ArticleCreateView',
    component: ArticleCreateView
  },
  {
    path: '/community/:id',
    name: 'ArticleDetailView',
    component: ArticleDetailView,
    props: route => ({id: Number(route.params.id)})
  },
  {
    path: '/community/:id/update',
    name: 'ArticleUpdateView',
    component: ArticleUpdateView,
    props: route => ({id: Number(route.params.id)})
  },
  {
    path: '/movies',
    name: 'MoviesView',
    component: MoviesView
  },
  {
    path: '/movies/genre/:genreName',
    name: 'GenreAllMovies',
    component: GenreAllMovies,
    props: route => ({genreName: String(route.params.genreName)})
  },
  {
    path: '/movie/:id/reviews',
    name: 'MovieReviewsView',
    component: MovieReviewsView,
    props: route => ({id: Number(route.params.id)})
  },
  {
    path: '/movie/:id',
    name: 'MovieDetailView',
    component: MovieDetailView,
    props: route => ({id: Number(route.params.id)})
  },
  {
    path: '/movie/:id/reviews/:reviewId',
    name: 'MovieReviewDetailView',
    component: MovieReviewDetailView,
    props: route => ({id: Number(route.params.id), reviewId: Number(route.params.reviewId)})
  },
  {
    path: '/movie/:id/review/create',
    name: 'MovieReviewCreate',
    component: MovieReviewCreate,
    props: route => ({id: Number(route.params.id)})
  },
  {
    path: '/movie/:id/reviews/:reviewId/update',
    name: 'MovieReviewUpdateView',
    component: MovieReviewUpdateView,
    props: route => ({id: Number(route.params.id), reviewId: Number(route.params.reviewId)})
  },
  {
    path: '/movie/search/:searchWord',
    name: 'MovieSearchView',
    component: MovieSearchView,
    props: route => ({searchWord: String(route.params.searchWord)})
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
