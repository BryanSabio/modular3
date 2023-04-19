from rest_framework import routers
from api.views import ProductopViewSet, ProductomViewSet, ProductogViewSet, ProductoGViewSet,UserViewSet, LogoutView , LoginView
from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path
router  = routers.DefaultRouter()
router.register('productopequeno', ProductopViewSet)
router.register('productomediano', ProductomViewSet)
router.register('productogrande', ProductogViewSet)
router.register('productogigante',ProductoGViewSet)
router.register('user', UserViewSet)

urlpatterns = [
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),
] + router.urls

