from django.urls import path
from .views import PhotoDetail, GetUploadURL

urlpatterns = [
    path("photos/get-url", GetUploadURL.as_view()),
    path("photos/get-photos", PhotoDetail.as_view()),
]
