from rest_framework import serializers, fields
from ...models import User

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('identification', 'first_name', 'last_name','email')

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        return user