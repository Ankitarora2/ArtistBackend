from rest_framework import serializers
from .models import Artist, Work, Client, User


class WorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Work
        fields = ['id', 'link', 'work_type']


class ArtistSerializer(serializers.ModelSerializer):
    works = WorkSerializer(many=True)

    class Meta:
        model = Artist
        fields = ['id', 'name', 'works']


class WorkListSerializer(serializers.ListSerializer):
    def to_representation(self, data):
        data = data.filter(user_instance=self.context['request'].user)
        return super(WorkListSerializer, self).to_representation(data)


class WorkCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Work
        fields = ['link', 'work_type']


class ClientCreateSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user_instance.username')
    password = serializers.CharField(write_only=True, style={'input_type': 'password'})

    class Meta:
        model = Client
        fields = ['name', 'username', 'password']

    def create(self, validated_data):
        username = validated_data.pop('user_instance')['username']
        password = validated_data.pop('user_instance')['password']
        user = User.objects.create_user(username=username, password=password)
        client = Client.objects.create_client_for_user(user)
        return client
