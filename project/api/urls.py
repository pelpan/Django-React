from django.urls import path, include
from .views import RoomView, RoomQuery

urlpatterns = [
    # Link a url to a APIView
    path('room', RoomView.as_view()),
    path('list', RoomQuery.as_view())
]