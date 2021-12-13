from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from rest_framework import viewsets
from rest_framework.decorators import action

from apps.favorites.serializers import FavoriteSerializer
from rest_framework_simplejwt.views import TokenObtainPairView as SimpleTokenObtainPairView
from apps.carts.serializers import CartSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from apps.users.serializers import UserSerializer, UserCreateSerializer, TokenObtainPairSerializer

User = get_user_model()


class TokenObtainPairView(SimpleTokenObtainPairView):
    serializer_class = TokenObtainPairSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_serializer_class(self):
        if self.action in ['create']:
            return UserCreateSerializer
        return self.serializer_class

    @action(detail=True, methods=['get'])
    def favorites(self, request, pk=None):
        user = self.get_object()
        favorites = user.favorites.all()
        page = self.paginate_queryset(favorites)
        if page is not None:
            serializer = FavoriteSerializer(favorites, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(favorites, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def carts(self, request, pk=None):
        user_current = self.get_object()
        carts = user_current.cart
        serializer = CartSerializer(carts)
        return Response(serializer.data)


@api_view(['GET'])
def current_user(request):
    serializer = UserSerializer(request.user)
    return Response(serializer.data)


def email_verify(request, email):
    if request.method == 'POST':
        email = request.POST.get('email_data')
        print(email)
        user = User.objects.get(email=email)
        user.is_active = True
        user.save()
        return redirect('http://89.223.65.30/')
    return render(request, 'users/email-confirm.html', {'email': email})
