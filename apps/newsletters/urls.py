from rest_framework.routers import DefaultRouter
from apps.newsletters.views import GetEmailViewSet, MessageNewsletterViewsSet

router = DefaultRouter()
router.register('email', GetEmailViewSet, basename='get-email')
router.register('message', MessageNewsletterViewsSet, basename='message')

urlpatterns = router.urls
