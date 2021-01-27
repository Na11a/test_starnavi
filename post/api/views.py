from ..models import Like
from .serializers import LikeSerializer
from django.utils import timezone
from rest_framework import generics



class LikeListView(generics.ListAPIView):
    serializer_class = LikeSerializer
    def get_queryset(self):
        date_from = self.request.query_params.get("date_from")
        date_to = self.request.query_params.get("date_to",timezone.now())
        likes = Like.objects.filter(updated__range=(date_from,date_to))
        return likes

