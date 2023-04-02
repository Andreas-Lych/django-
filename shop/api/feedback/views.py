from rest_framework import viewsets

from api.feedback.serializers import FeedbackModelSerializer
from feedback.models import Feedback


class FeedbackViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows product to be viewed.
    """

    queryset = Feedback.objects.all().order_by("-created_at")
    serializer_class = FeedbackModelSerializer
    permission_classes = []
