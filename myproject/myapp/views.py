from rest_framework import generics, filters, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Artist, Work
from .serializers import ArtistSerializer, WorkSerializer, WorkCreateSerializer, ClientCreateSerializer


class WorkList(generics.ListAPIView):
    serializer_class = WorkSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['artist__name']
    ordering_fields = ['id']

    def get_queryset(self):
        queryset = Work.objects.all()
        work_type = self.request.query_params.get('work_type', None)
        artist = self.request.query_params.get('artist', None)
        if work_type is not None:
            queryset = queryset.filter(work_type=work_type)
        if artist is not None:
            queryset = queryset.filter(artist__name=artist)
        return queryset


class ArtistList(generics.ListAPIView):
    serializer_class = ArtistSerializer
    queryset = Artist.objects.all()


class WorkCreate(generics.CreateAPIView):
    serializer_class = WorkCreateSerializer

    def perform_create(self, serializer):
        serializer.save(artist=self.request.user.artist)


@api_view(['POST'])
def register(request):
    serializer = ClientCreateSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)
