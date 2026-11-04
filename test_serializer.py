import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portofolio.settings')
django.setup()

from main.models import Projects
from main.serializers import ProjectSerializer

projects = Projects.objects.all()
print("Projects data:", ProjectSerializer(projects, many=True).data)

candidate = ProjectSerializer(data={
    "title": "Portfolio", 
    "description": "My website", 
    "tech_stack": "Django",
})
print("Is valid:", candidate.is_valid())
print("Validated data:", candidate.validated_data)

invalid = ProjectSerializer(data={"title": ""})
print("Invalid is valid:", invalid.is_valid())
print("Errors:", invalid.errors)