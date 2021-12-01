from rest_framework_simplejwt import tokens
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class MyTokenPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token =  super().get_token(user)
        token['email'] = user.email
        token['username'] = user.username
        return token
