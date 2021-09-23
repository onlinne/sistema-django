from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from cerberus import Validator
from ...serializers import UserSerializer


class UserApi(APIView):
    #para obtener usuarios ->get http://127.0.0.1:8000/usysAPI/users
    def get(self, request):
        serializer = UserSerializer()
        users = serializer.get_users()

        #no hay usuarios(?)
        if users== None:
            return Response({
                'message': 'no hay usuarios registrados',
            }, status=status.HTTP_204_NO_CONTENT)

        return Response(
            {
                'data': users
            }, status=status.HTTP_200_OK)

    #para crear usuarios -> post http://127.0.0.1:8000/usysAPI/users
    def post(self, request):
        validator = Validator({
            'username': {'required': True, 'type': 'string'},
            'first_name': {'required': True, 'type': 'string'},
            'last_name': {'required': True, 'type': 'string'},
            'email':{'required':True, 'type':'string'},
            'password':{'required':True,'type':'string'},
        })
        if not validator.validate(request.data):
            return Response({
                'errors': validator.errors,
            }, status=status.HTTP_400_BAD_REQUEST)

        serializer = UserSerializer()
        serializer.create(request.data)

        return Response("Usuario creado",status=status.HTTP_201_CREATED)
    
    def delete_user(self,request):
        validator = Validator({
            'username': {'required': True, 'type': 'string'},
            'is_active':{'required':True, 'type':'integet','max_length':1}
        })

        if not validator.validate(request.data):
            return Response({'errors': validator.errors}, 
            status=status.HTTP_400_BAD_REQUEST)

        if not request.GET.get('username'):
            return Response({'error': 'CODIGO requerido'}, 
            status=status.HTTP_400_BAD_REQUEST)
        
        serializer = UserSerializer()
        print(request.GET['username'])
        print(type(request.GET['username']))
        serializer.remove_users(int(request.GET['username']), request.data)

    # def delete(self, request):
    #     if not request.GET.get('username'):
    #         return Response({
    #             'errors': 'se requiere el CODIGO del usuario'
    #         }, status=status.HTTP_400_BAD_REQUEST)

    #     serializer = UserSerializer()
    #     deleted = serializer.remove_users(request.GET.get('username'))
    #     return Response({
    #         'eliminado': deleted
    #     },status=status.HTTP_200_OK)
