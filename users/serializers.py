from rest_framework import serializers
from django.contrib.auth import authenticate

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)

            if user:
                data['user'] = user
            else:
                raise serializers.ValidationError("ma'lumotlarni tekshiring ular hato berilgan")
        else:
            raise serializers.ValidationError("username va password kiritilishi shart ")

        return data 


