from django.contrib.auth import get_user_model
from rest_framework import views, permissions, status
from rest_framework.response import Response

# from .serializers import ObtainTokenSerializer
# from .authentication import JWTAuthentication

# User = get_user_model()

# class ObtainTokenView(views.APIView):
#     permission_classes = [permissions.AllowAny]
#     serializer_class = ObtainTokenSerializer

#     def post(self, request):
#         serializer = self.serializer_class(data=request.data)
#         serializer.is_valid(raise_exception=True)

#         email = serializer.validated_data.get("email")
#         password = serializer.validated_data.get("password")

#         user = User.objects.filter(email=email).first()

#         if user is None or not user.check_password(password):
#             return Response(
#                 {"message": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST
#             )

#         # Generate the JWT token
#         jwt_token = JWTAuthentication.create_jwt(user)

#         return Response({"token": jwt_token})

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import CustomUserSerializer

CustomUser = get_user_model()

class RegisterView(APIView):

    def post(self, request):
        data = request.data
        
        serializer = CustomUserSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        
        email = serializer.data['email']
        password = serializer.data['password']
        name = serializer.data['name']

        CustomUser.objects.create_user(email, password, name)

        response = Response()
        response.data = {
            'message': 'User Created Successfully',
            'data': serializer.data
        }

        return response
    
class CustomUserView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = CustomUserSerializer(request.user)
        return Response(serializer.data)
