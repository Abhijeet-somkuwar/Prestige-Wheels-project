from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

class LoginSerializer(serializers.Serializer):
    """
    Serializer for user login.
    Takes username and password and validates them.
    """
    username = serializers.CharField(max_length=150)
    password = serializers.CharField(write_only=True)
    
    def validate(self, data):
        """
        Validate that the username and password are correct
        """
        username = data.get('username')
        password = data.get('password')
        
        # Authenticate the user
        user = authenticate(username=username, password=password)
        
        if not user:
            raise serializers.ValidationError("Invalid username or password")
        
        data['user'] = user
        return data


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for User model - returns user info after successful login
    """
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']
