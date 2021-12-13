from rest_framework import serializers
from utils.celery_tasks import send_newsletter
from apps.newsletters.models import GetEmail, MessageNewsletter


class GetEmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = GetEmail
        fields = "__all__"


class MessageNewsletterSerializer(serializers.ModelSerializer):
    class Meta:
        model = MessageNewsletter
        fields = "__all__"

    def create(self, validated_data):
        message = MessageNewsletter.objects.create(**validated_data)
        send_newsletter.delay(message.text)
        return message
