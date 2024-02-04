from django.urls import path

from notice.views import NoticesAPIView, NoticeAPIView, CommentsAPIView, CommentAPIView, EmotionAPIView

urlpatterns = [
    path('notice/', NoticesAPIView.as_view()),
    path('notice/<int:pk>/', NoticeAPIView.as_view()),
    path('notice/<int:pk>/comment/', CommentsAPIView.as_view()),
    path('notice/<int:pk>/comment/<int:comment_id>/', CommentAPIView.as_view()),
    path('notice/<int:pk>/like/', EmotionAPIView.as_view())
]
