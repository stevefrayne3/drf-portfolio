from rest_framework import serializers

from .models import Project,Contact


# Project Serializer
class ProjectSerializer(serializers.ModelSerializer):
    class Meta :
        model = Project
        fields = '__all__'


# Contact Serailizer
class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'