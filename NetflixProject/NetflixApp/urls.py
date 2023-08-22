from django.urls import path
from .views import Home,ProfileList,ProfileCreate,Watch,ShowMovieDetails,ShowMovie

appName = "NetflixApp"

urlpatterns = [
    path('', Home.as_view()),
    path('profile/', ProfileList.as_view(), name="profileList"),
    path("profile/create/",ProfileCreate.as_view(), name="profileCreate"),
    path("watch/<str:profile_id>/",Watch.as_view(), name="watch"),
    path('movie/detail/<str:movie_id>/', ShowMovieDetails.as_view(), name="showDetails"),
    path("movie/play/<str:movie_id>/", ShowMovie.as_view(), name='play'),

]