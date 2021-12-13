from rest_framework import viewsets
from apps.main_pages.models import MainPage
from apps.main_pages.serializers import MainPageSerializer, MainPageCreateSerializer


class MainPageViewSet(viewsets.ModelViewSet):
    queryset = MainPage.objects.all().select_related(
        'categories__parent',
    )
    serializer_class = MainPageSerializer

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return self.serializer_class
        return MainPageCreateSerializer
