from django.shortcuts import render
from .models import Mahasiswa
from .models import Experience
from .models import Education
from .models import Skills
from .models import Projects

def index(request):
    mahasiswas = Mahasiswa.objects.all()

    context = {'mahasiswas' : mahasiswas}

    return render(request, 'index.html', context)

def show_main(request):
    context = {
        "name": "Andrew Chandra Halim",
        "npm": "2506656431",
        "study_program": "S1 Ilmu Komputer",
        "bio": (
            "Mahasiswa Ilmu Komputer Universitas Indonesia yang tertarik "
            "pada pengembangan perangkat lunak dan pendidikan."
        ),
    }
    return render(request, "index.html", context)


def show_experience(request):
    context = {
        "name": "Andrew Chandra Halim",
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)

def show_education(request):
    context = {
        "name": "Andrew Chandra Halim",
        "education_list": Education.objects.all(),
    }
    return render(request, "education.html", context)

def show_skills(request):
    context = {
        "name": "Andrew Chandra Halim",
        "skills_list": Skills.objects.all(),
    }
    return render(request, "skills.html", context)

def show_projects(request):
    context = {
        "name": "Andrew Chandra Halim",
        "projects_list": Projects.objects.all(),
    }
    return render(request, "projects.html", context)