from django.urls import path

from file_upload.views import *



urlpatterns = [
    path('', index, name='home'),
    path('files/', FileViewSet.as_view({'get':'list'}), name='File_list'),
    path('upload/', FileViewSet.as_view({'post': 'create'}), name='File_uploads'),
    # path('upload/', FileAPIView.as_view()),
]