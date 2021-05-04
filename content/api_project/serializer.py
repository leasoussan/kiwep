from rest_framework.serializers import ModelSerializer

from content.models import Project 


class ProjectCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = [
            'id',
            'name',
            'title',
            'description',
            'required_skills',
            'acquried_skills',
            'time_to_complet',
            'field',
            'difficulty',
            'completed',
            'speaker',
            'missions',
            'points',
        ] 



class ProjectListSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = [
            'id',
            'name',
            'title',
            'description',
            'required_skills',
            'acquried_skills',
            'time_to_complet',
            'field',
            'difficulty',
            'completed',
            'speaker',
            'missions',
            'points',
        ] 



class ProjectDetailSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = [
            'id',
            'name',
            'title',
            'description',
            'required_skills',
            'acquried_skills',
            'time_to_complet',
            'field',
            'difficulty',
            'completed',
            'speaker',
            'missions',
            'points',
        ] 