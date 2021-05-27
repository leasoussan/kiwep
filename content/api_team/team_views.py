from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView,
    CreateAPIView,
    RetrieveUpdateAPIView,
)

from rest_framework.response import Response
from rest_framework.decorators import api_view

from content.models import Team
from .team_serializer import (
    TeamListSerializer,
    TeamDetailSerializer,
    TeamCreateUpdateSerializer,
)


@api_view(['GET'])
def projectOverview(request):
    team_urls = {
        'List': '/team_list/',
        'Detail View': '/team_detail/<str:pk>/',
        'Create': '/team_create/',
        'Update': '/team_update/<str:pk>/',
        'Delete': '/team_delete/<str:pk>/',
    }
    return Response(team_urls)


class TeamCreateAPIView(CreateAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamCreateUpdateSerializer

    # def perform_create(self, serializer):
    #     serializer.save(manager=self.request.user)


class TeamDetailAPIView(RetrieveAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamDetailSerializer

    # if we want to change the lookup in url
    # lookup_url_kwarg = "What I want to "/


class TeamUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamCreateUpdateSerializer

    # def perform_update(self, serializer):
    #     serializer.save(manager=self.request.user)


class TeamDeleteAPIView(DestroyAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamDetailSerializer


class TeamListAPIView(ListAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamListSerializer
