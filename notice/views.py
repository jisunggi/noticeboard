from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError
from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from notice.models import Notice, Comment, Emotion
from notice.serializers import NoticeSimpleSerializer, NoticeCreateSerializer, NoticeDetailSerializer, \
    CommentCreateSerializer, CommentsSerializer, CommentDetailSerializer, EmotionSerializer


# Create your views here.

class NoticesAPIView(APIView):

    def get(self, request):
        notices = Notice.objects.all()
        serializer = NoticeSimpleSerializer(notices, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = NoticeCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class NoticeAPIView(APIView):

    def get(self, request, pk):
        notice = get_object_or_404(Notice, id=pk)
        notice.views += 1
        notice.save()
        serializer = NoticeDetailSerializer(notice)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, pk):
        notice = get_object_or_404(Notice, id=pk)
        password = request.data.get('password')
        if password == notice.password:
            serializer = NoticeDetailSerializer(notice, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'error': '비밀번호가 일치하지 않습니다.'}, status=status.HTTP_403_FORBIDDEN)

    def delete(self, request, pk):
        notice = get_object_or_404(Notice, id=pk)
        password = request.query_params.get('password', None)
        if not password:
            return Response({'error': '비밀번호를 입력해주세요.'}, status=status.HTTP_403_FORBIDDEN)
        if password == notice.password:
            notice.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response({'error': '비밀번호가 일치하지 않습니다.'}, status=status.HTTP_403_FORBIDDEN)


class CommentsAPIView(APIView):

    def post(self, request, pk):
        notice = get_object_or_404(Notice, id=pk)
        serializer = CommentCreateSerializer(data={'notice_id': notice.id,'description': request.data['description']})

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk):
        notice = get_object_or_404(Notice, id=pk)
        comments = Comment.objects.filter(notice_id=notice.id)
        serializer = CommentsSerializer(comments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CommentAPIView(APIView):

    def get(self, request, pk, comment_id):
        notice = get_object_or_404(Notice, id=pk)
        comment = get_object_or_404(Comment, id=comment_id)
        serializer = CommentDetailSerializer(comment)
        return Response(serializer.data, status=status.HTTP_200_OK)


class EmotionAPIView(APIView):

    def post(self, request, pk):
        notice = get_object_or_404(Notice, id=pk)
        user = request.data['user']

        if Emotion.objects.filter(notice_id=notice.id, user=user).exists():
            return Response({'error': '이미 좋아요나 싫어요를 눌렀습니다'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = EmotionSerializer(data={'notice_id': notice.id, 'user': user})

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        notice = get_object_or_404(Notice, id=pk)

        try:
            emotion = Emotion.objects.get(notice_id=notice.id, user=request.data['user'])
        except ObjectDoesNotExist:
            return Response({'error': '이름을 다시 확인하세요'}, status=status.HTTP_204_NO_CONTENT)

        if emotion.like:
            emotion.like = False
        else:
            emotion.like = True

        emotion.save()
        serializer = EmotionSerializer(emotion)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def get(self, request, pk):
        notice = get_object_or_404(Notice, id=pk)
        emotion = Emotion.objects.filter(notice_id=notice.id)
        serializer = EmotionSerializer(emotion, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)




