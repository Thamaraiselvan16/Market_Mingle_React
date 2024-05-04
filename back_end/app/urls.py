from django.urls import path
from app import views
# simple JWT
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    # TokenRefreshView,
)



urlpatterns = [
    path("",views.getRoutes,name="getRoutes"),
    path("products/",views.getProducts, name="products"),
    path("products/<str:pk>/",views.getProduct, name="products/id"),
    # simple JWT
    path('user/profile/',views.getUserProfiles,name="getUserProfiles"),
    path('users/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('users/',views.getUsers, name="getUsers"),
    path('users/register/',views.registerUser, name="register")

]