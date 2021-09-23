from rest_framework import serializers, fields
from ...models import User

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name','email')

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        return user

    def get_users(self):
        return UserSerializer(User.objects.all(), many=True).data

    def remove_users(self, username, validate_data):
        user = User.objects.update(
            username=int(username)).update(**validate_data)
        return user