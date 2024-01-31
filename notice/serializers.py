from rest_framework import serializers

from notice.models import Notice


class NoticeSimpleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Notice
        fields = ('id', 'title', 'created', 'views')


class NoticeCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notice
        fields = ('title', 'description')