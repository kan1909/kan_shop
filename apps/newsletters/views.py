from rest_framework import viewsets
from apps.newsletters.models import (
    GetEmail,
    MessageNewsletter,
)
from apps.newsletters.serializers import (
    MessageNewsletterSerializer,
    GetEmailSerializer,
)


class GetEmailViewSet(viewsets.ModelViewSet):
    queryset = GetEmail.objects.all()
    serializer_class = GetEmailSerializer


class MessageNewsletterViewsSet(viewsets.ModelViewSet):
    queryset = MessageNewsletter.objects.all()
    serializer_class = MessageNewsletterSerializer
