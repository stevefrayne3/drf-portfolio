
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework import viewsets

from .models import  Project ,Contact
from .serializers import  ContactSerializer, ProjectSerializer



# Create your views here.

# Projects view
@api_view(['GET'])
def ProjectsView(request):
    projects = Project.objects.all()
    serializer = ProjectSerializer(projects ,many=True)

    return Response(serializer.data ,status=status.HTTP_200_OK)


# Contact View
@api_view(['GET'])
def ContactView(request):
    contacts = Contact.objects.all()
    serializer = ContactSerializer(contacts ,many=True)

    return Response(serializer.data ,status=status.HTTP_200_OK)



# class ProjectViewset(viewsets.ModelViewSet):
#     queryset = Project.objects.all()
#     serializer_class = ProjectSerializer