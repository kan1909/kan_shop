from rest_framework import viewsets
from apps.favorites.models import Favorite
from apps.favorites.serializers import FavoriteSerializer, FavoriteCreateSerializer


class FavoriteViewSet(viewsets.ModelViewSet):
    queryset = Favorite.objects.all().prefetch_related(
        'products__favorites', 'products__favorites__user',
    )
    serializer_class = FavoriteSerializer

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return self.serializer_class
        return FavoriteCreateSerializer
