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
            'acquired_skills',
            'time_to_complete',
            'field',
            'difficulty',
            'completed',
            'speaker',
            'points',
            'is_template',
            'is_global',
            'is_premium',
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
            'acquired_skills',
            'time_to_complete',
            'field',
            'difficulty',
            'completed',
            'speaker',
            'points',
            'is_template',
            'is_global',
            'is_premium',
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
            'acquired_skills',
            'time_to_complete',
            'field',
            'difficulty',
            'completed',
            'speaker',
            'points',
            'is_template',
            'is_global',
            'is_premium',
        ]
