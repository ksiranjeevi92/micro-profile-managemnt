from django.urls import path, include
from rest_framework.routers import DefaultRouter


from profiles_api import views

router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, basename='hello-viewset')
router.register('user-profile', views.UserProfileViewSet)

urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),
    path('', include(router.urls)),
     path('login/', views.UserLoginApiView.as_view()),
]