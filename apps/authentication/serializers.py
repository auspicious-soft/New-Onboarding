from rest_framework import serializers
from apps.authentication.models import Profile
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
User = get_user_model()


class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255, min_length=3)
    password = serializers.CharField(max_length=68, min_length=8, write_only=True)
    username = serializers.CharField(max_length=255, min_length=3, read_only = True)
    tokens = serializers.CharField(max_length=68, min_length=8, read_only = True)


    class Meta:
        model = User
        fields = ['email', 'password', 'username', 'tokens']


    def validate(self, attrs):
        username = attrs.get('username', '')
        password = attrs.get('password', '')
  
        user = authenticate(username=username, password=password)

        if not user:
            msg = "Incorrect Username / Password please try again."
            raise serializers.ValidationError(msg, code='authorization')
        
        if not user.is_active:
            msg = 'Acccount disabled, please contact admin'
            raise serializers.ValidationError(msg, code='authorization')
 
        return {
            'email': user.email,
            'username': user.username,
            'tokens': user.tokens
        }
        
        return super().validate(attrs)