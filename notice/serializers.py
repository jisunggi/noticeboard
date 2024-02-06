from rest_framework import serializers

from notice.models import Notice, Comment, Emotion


class NoticeSimpleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Notice
        fields = ('id', 'title', 'description', 'created', 'views')


class NoticeCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notice
        fields = ('title', 'description', 'password')


class NoticeDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Notice
        fields = ('id', 'title', 'description', 'created', 'views')


class CommentCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ('notice_id', 'description')


class CommentsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ('description', 'created')


class CommentDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('notice_id', 'description', 'created')


class EmotionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Emotion
        fields = ('notice_id', 'user', 'like')


