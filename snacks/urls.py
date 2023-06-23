from django.urls import path
from .views import HomePageView,AboutPageView,SnackListView,SnackDetailsView

urlpatterns = [
    path('',HomePageView.as_view(), name='home'),
    path('about-us',AboutPageView.as_view(), name='about'),
    path('snack-list',SnackListView.as_view(), name='snack-list'),
    path('<int:pk>/',SnackDetailsView.as_view(), name='snack-detail')
]