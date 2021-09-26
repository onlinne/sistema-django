from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from cerberus import Validator
from ...serializers import UserSerializer
import re



class UserApi(APIView):

    def post(self, request):
        validator = Validator({
            'identification': {
                'required': True, 
                'type': 'string',
                'regex':'[1-9][0-9]{6,10}'
                },
            'first_name': {'required': True, 'type': 'string'},
            'last_name': {'required': True, 'type': 'string'},
            'email':{
                'required':True,
                'type':'string',
                'regex':r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'},
            'password':{'required':True,'type':'string'},
        })

        if not validator.validate(request.data):
            return Response({
                'errors': validator.errors,
            }, status=status.HTTP_400_BAD_REQUEST)

        serializer = UserSerializer()
        serializer.create(request.data)

        return Response("Usuario creado",status=status.HTTP_201_CREATED)
