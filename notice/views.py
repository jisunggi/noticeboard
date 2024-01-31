from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from notice.models import Notice
from notice.serializers import NoticeSimpleSerializer, NoticeCreateSerializer, NoticeDetailSerializer


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
        password = request.data.get('password')
        if password == notice.password:
            notice.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response({'error': '비밀번호가 일치하지 않습니다.'}, status=status.HTTP_403_FORBIDDEN)