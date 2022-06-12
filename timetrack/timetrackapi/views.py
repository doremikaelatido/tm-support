from django.shortcuts import render
from django.db.models import Count
from django.http import HttpResponse

from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser, FormParser, FileUploadParser
from rest_framework import views

from .serializers import ProjectSerializer, UserSerializer, WorkLogSerializer
from .models import User, WorkLog, Project

from .util.ingestDataUtil import *
from rest_framework.decorators import action

import json

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class WorkLogViewSet(viewsets.ModelViewSet):
    queryset = WorkLog.objects.all()
    serializer_class = WorkLogSerializer

    @action(detail=True, methods=['get'], url_path=r'(?P<username>\w+)')    
    def userlogs(self, request, username, pk=None):
        userFilter = User.objects.filter(username=username)[0]
        if not userFilter:
            raise Exception("User does not exist....")

        worklogs = self.get_queryset()
        logs = worklogs.filter(user=userFilter)
        serializer = self.get_serializer(logs, many=True)
        return HttpResponse(json.dumps(serializer.data))


class FileUploadView(views.APIView):
    parser_classes = [FileUploadParser]

    def post(self, request, format='csv'):
        up_file = request.FILES['file']

        path = default_storage.save('worklog.csv', ContentFile(up_file.read()))
        tmp_file = os.path.join(settings.MEDIA_ROOT, path)
        
        ingestData(tmp_file)
        
        path = default_storage.delete(tmp_file)

        return HttpResponse(status=201)