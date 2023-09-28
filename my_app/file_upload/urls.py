from django.urls import path

from file_upload.views import *



urlpatterns = [
    path('files/', FileViewSet.as_view({'get':'list'})),
    path('upload/', FileViewSet.as_view({'post': 'create'})),
    # path('upload/', FileAPIView.as_view()),
]