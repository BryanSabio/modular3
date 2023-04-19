
from rest_framework import viewsets, permissions
from api.models import ProductoPequeno, ProductoMediano, ProductoGrande, ProductoGigante
from api.serializers import ProductopSerializer, ProductomSerializer, ProductogSerializer, ProductoGSerializer, UserSerializer
from rest_framework import status,views, response
from rest_framework import authentication
from django.contrib.auth.models import User
from django.contrib.auth import logout ,authenticate, login 
from rest_framework.authtoken.models import Token

class ProductopViewSet(viewsets.ModelViewSet):
    queryset = ProductoPequeno.objects.all()
    serializer_class = ProductopSerializer
    permission_classes = [permissions.AllowAny]

class ProductomViewSet(viewsets.ModelViewSet):
    queryset = ProductoMediano.objects.all()
    serializer_class = ProductomSerializer
    permission_classes = [permissions.AllowAny]

class ProductogViewSet(viewsets.ModelViewSet):
    queryset = ProductoGrande.objects.all()
    serializer_class = ProductogSerializer
    permission_classes = [permissions.AllowAny]

class ProductoGViewSet(viewsets.ModelViewSet):
    queryset = ProductoGigante.objects.all()
    serializer_class = ProductoGSerializer
    permission_classes = [permissions.AllowAny]



class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser,]
    authentication_classes = [authentication.BasicAuthentication,]

class LoginView(views.APIView):
    permission_classes = [permissions.AllowAny]
    def post(self, request):
        # Recuperamos las credenciales y autenticamos al usuario
        username2= request.data.get('username', None)
        password2 = request.data.get('password', None)
        if username2 is None or password2 is None:
            return response.Response({'message': 'Please provide both username and password'},status=status.HTTP_400_BAD_REQUEST)
        user2 = authenticate(username=username2, password=password2)
        if not user2:
            return response.Response({'message': 'Usuario o Contraseña incorrecto !!!! '},status=status.HTTP_404_NOT_FOUND)

        token, _ = Token.objects.get_or_create(user=user2)
        # Si es correcto añadimos a la request la información de sesión
        if user2:
            # para loguearse una sola vez
            # login(request, user)
            return response.Response({'message':'usuario y contraseña correctos!!!!'},status=status.HTTP_200_OK)
            #return response.Response({'token': token.key}, status=status.HTTP_200_OK)

        # Si no es correcto devolvemos un error en la petición
        return response.Response(status=status.HTTP_404_NOT_FOUND)        

class LogoutView(views.APIView):
    authentication_classes = [authentication.TokenAuthentication]
    def post(self, request):        
        request.user.auth_token.delete()
        # Borramos de la request la información de sesión
        logout(request)
        # Devolvemos la respuesta al cliente
        return response.Response({'message':'Sessión Cerrada'},status=status.HTTP_200_OK)