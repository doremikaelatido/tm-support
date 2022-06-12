from rest_framework import serializers

from .models import Project, User, WorkLog

class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'projectname')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')

class WorkLogSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.SlugRelatedField(
        slug_field='username',
        queryset=User.objects.all()
    )

    project = serializers.SlugRelatedField(
        slug_field='projectname',
        queryset=Project.objects.all()
    )

    class Meta:
        model = WorkLog
        fields = ('id', 'user', 'project', 'start_time', 'end_time', 'hours_spent')