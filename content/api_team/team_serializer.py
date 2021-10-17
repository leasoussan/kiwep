from rest_framework.serializers import ModelSerializer

from content.models import Team


class TeamCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = Team
        fields = [
            'id',
            'name',
            'project',
            'start_date',
            'group_institution',
            'participants',
            'manager',
            'project_completed',
        ]

class TeamListSerializer(ModelSerializer):
    class Meta:
        model = Team
        fields = [
            'id',
            'name',
            'project',
            'start_date',
            'group_institution',
            'participants',
            'manager',
            'project_completed',
        ]

class TeamDetailSerializer(ModelSerializer):
    class Meta:
        model = Team
        fields = [
            'id',
            'name',
            'project',
            'start_date',
            'group_institution',
            'participants',
            'manager',
            'project_completed',
        ]
