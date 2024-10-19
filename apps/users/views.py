from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status

from apps.users.models import User
from apps.users.serializers import UserLoginSerializer, UserRegister
# Create your views here.

class UserAPI(GenericViewSet,
              mixins.ListModelMixin,
              mixins.CreateModelMixin,
              mixins.UpdateModelMixin,
              mixins.RetrieveModelMixin,
              mixins.DestroyModelMixin):
    queryset = User.objects.all()
    serializer_class = UserRegister


class LoginViewSet(mixins.CreateModelMixin,
                    GenericViewSet):
    serializer_class = UserLoginSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.id,
            'email': user.email
        }, status=status.HTTP_200_OK)