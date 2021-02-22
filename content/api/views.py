from rest_framework.generics import (
    ListAPIView, 
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView,
    CreateAPIView,
    RetrieveUpdateAPIView,
)

from content.models import Project 
from .serializer import (
    ProjectListSerializer, 
    ProjectDetailSerializer, 
    ProjectCreateUpdateSerializer
,
)



class ProjectCreateAPIView(CreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectCreateUpdateSerializer

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
    

class ProjectDetailAPIView(RetrieveAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectDetailSerializer
    
    # if we want to change the lookup in url
    # lookup_url_kwarg = "What I want to "/


class ProjectUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectCreateUpdateSerializer
    
    def perform_update(self, serializer):
        serializer.save(created_by=self.request.user)
    


class ProjectDeleteAPIView(DestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectDetailSerializer
    


class ProjectListAPIView(ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectListSerializer


