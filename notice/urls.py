from django.urls import path

from notice.views import NoticesAPIView, NoticeAPIView

urlpatterns = [
    path('notice/', NoticesAPIView.as_view()),
    path('notice/<int:pk>/', NoticeAPIView.as_view())
]
