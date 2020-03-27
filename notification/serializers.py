from datetime import datetime

from django.utils.timezone import utc
from rest_framework import serializers

from notification.models import Notification
from user.models import User
from user.serializers import UserSerializer


class NotificationCreateSerializer(serializers.ModelSerializer):
    creation_date = serializers.HiddenField(default=datetime.now(tz=utc))
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())
    is_completed = serializers.HiddenField(default=False)

    def validate_completion_date(self, value):
        if value < datetime.now(tz=utc):
            raise serializers.ValidationError("Неверная Дата наступления.")
        return value

    class Meta:
        model = Notification
        fields = '__all__'


class NotificationSerializer(serializers.ModelSerializer):
    creation_date = serializers.ReadOnlyField(default=datetime.now(tz=utc))
    owner = UserSerializer(read_only=True)
    recipients = UserSerializer(many=True)

    class Meta:
        model = Notification
        fields = '__all__'


class NotificationUpdateSerializer(serializers.ModelSerializer):
    recipients = serializers.PrimaryKeyRelatedField(many=True,
                                                    queryset=User.objects.all())

    class Meta:
        model = Notification
        fields = ('id', 'title', 'description', 'place',
                  'completion_date', 'recipients', 'is_completed')
