from .serializers import MyTokenObtainPairSerializer, ChangePasswordSerializer, CustomUserSerializer
from .models import CustomUser
from rest_framework import generics, status, permissions, response, filters, pagination, response
from rest_framework_simplejwt import views
from rest_framework.views import APIView

#Token Serializer
class MyTokenObtainPairView(views.TokenViewBase):
    serializer_class = MyTokenObtainPairSerializer

#Password change View
class ChangePasswordView(generics.UpdateAPIView):
    """
    An endpoint for changing password.
    """
    serializer_class = ChangePasswordSerializer
    model = CustomUser
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj
        
    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            # Check old password
            if not self.object.check_password(serializer.data.get("old_password")):
                return response.Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            resp = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Password updated successfully',
                'data': []
            }
            return response.Response(resp)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class CustomUserPagination(pagination.LimitOffsetPagination):
    default_limit = 5
    max_limit = 100

class RegisterView( APIView):
    permission_classes = (permissions.AllowAny,) #required for new user registration
    def post( self, request):
        serializer = CustomUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)         
        serializer.save()
        return response.Response(serializer.data)
