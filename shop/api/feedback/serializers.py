from rest_framework import serializers

from feedback.models import Feedback


class FeedbackModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Feedback
        fields = ["title", "text", "created_at"]

