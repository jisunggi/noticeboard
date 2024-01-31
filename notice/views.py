from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from notice.models import Notice
from notice.serializers import NoticeSimpleSerializer, NoticeCreateSerializer


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