from rest_framework.serializers import ModelSerializer

from content.models import Resource


class ResourceCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = Resource
        fields = [
            'id',
            'name',
            'link',
            'image',
            'file_rsc',
            'text',
            'owner',
            'field',
        ]



class ResourceListSerializer(ModelSerializer):
    class Meta:
        model = Resource
        fields = [
            'id',
            'name',
            'link',
            'image',
            'file_rsc',
            'text',
            'owner',
            'field',
        ]



class ResourceDetailSerializer(ModelSerializer):
    class Meta:
        model = Resource
        fields = [
            'id',
            'name',
            'link',
            'image',
            'file_rsc',
            'text',
            'owner',
            'field',
        ]
