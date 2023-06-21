from django.shortcuts import get_object_or_404
from rest_framework.views import APIView, Response, status
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Song
from rest_framework.pagination import PageNumberPagination
from .serializers import SongSerializer
from albums.models import Album
from rest_framework import generics


class SongView(generics.ListCreateAPIView):
    serializer_class = SongSerializer
    queryset = Song.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [JWTAuthentication]

    def get_queryset(self):
        pk = self.kwargs['pk']
        return Song.objects.filter(album_id=pk)

    def perform_create(self, serializer):
        pk = self.kwargs['pk']
        album = get_object_or_404(Album, pk=pk)
        serializer.save(album=album)