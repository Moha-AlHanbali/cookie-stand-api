from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers import MyTokenPairSerializer

class MyTokenObtainedPairCustomView(TokenObtainPairView):
    serializer_class = MyTokenPairSerializer
