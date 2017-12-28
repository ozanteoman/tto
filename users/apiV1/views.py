from rest_framework.generics import CreateAPIView,GenericAPIView
from .serializers import UserCreateSerializer,UserLoginSerializer

from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK,HTTP_400_BAD_REQUEST

class UserCreateApiView(CreateAPIView):
    serializer_class = UserCreateSerializer

class UserLoginApiView(GenericAPIView):
    serializer_class = UserLoginSerializer
    permission_classes = [AllowAny]

    def post(self,request,*args,**kwargs):
        serializer=self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            new_data=serializer.data
            return Response(data=new_data,status=HTTP_200_OK)
        return Response(data=serializer.errors,status=HTTP_400_BAD_REQUEST)



