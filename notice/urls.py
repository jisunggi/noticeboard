from django.urls import path

from notice.views import NoticesAPIView

urlpatterns = [
    path('notice/', NoticesAPIView.as_view()),
]
