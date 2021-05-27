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

from content.models import Project
from .project_serializer import (
    ProjectListSerializer,
    ProjectDetailSerializer,
    ProjectCreateUpdateSerializer,
)


@api_view(['GET'])
def projectOverview(request):
    project_urls = {
        'List': '/project_list/',
        'Detail View': '/project_detail/<str:pk>/',
        'Create': '/project_create/',
        'Update': '/project_update/<str:pk>/',
        'Delete': '/project_delete/<str:pk>/',
    }
    return Response(project_urls)



class ProjectCreateAPIView(CreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectCreateUpdateSerializer

    def perform_create(self, serializer):
        serializer.save()


class ProjectDetailAPIView(RetrieveAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectDetailSerializer

    # if we want to change the lookup in url
    # lookup_url_kwarg = "What I want to "/


class ProjectUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectCreateUpdateSerializer

    def perform_update(self, serializer):
        serializer.save()



class ProjectDeleteAPIView(DestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectDetailSerializer



class ProjectListAPIView(ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectListSerializer
