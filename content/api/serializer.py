from rest_framework.serializers import ModelSerializer

from content.models import Project 


class ProjectCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = [
            'id',
            'name',
            'description',
            'time_to_complet',
            'field',
            'difficulty',
            'mission'
        ] 



class ProjectListSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = [
            'id',
            'name',
            'description',
            'time_to_complet',
            'field',
            'difficulty',
            'mission'
        ] 



class ProjectDetailSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = [
            'id',
            'name',
            'description',
            'time_to_complet',
            'field',
            'difficulty',
            'mission'
        ] 