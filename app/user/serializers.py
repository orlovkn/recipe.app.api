from django.contrib.auth import get_user_model

from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    """Serializer forthe users object"""

    class Meta:
        model = get_user_model()
