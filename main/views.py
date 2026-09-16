from .models import Mahasiswa
from .models import Experience
from .models import Education
from .models import Skills
from .models import Projects
from .forms import EducationForm
from django.contrib import messages
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render


def create_Education(request):
    form = EducationForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Data baru berhasil ditambahkan!")
        return redirect("main:show_education")

    context = {
        "name": "Andrew Chandra Halim",
        "form": form,
    }
    return render(request, "education_form.html", context)

def delete_education(request, education_id):
    education = get_object_or_404(Education, pk=education_id)

    if request.method == "POST":
        education.delete()
        messages.success(request, "Education berhasil dihapus!")
        return redirect("main:show_education")

    return redirect("main:show_education")

def get_educations_json(request):
    title_query = request.GET.get("title", "").strip()
    educations = Education.objects.all()

    if title_query:
        educations = educations.filter(description__icontains=title_query)

    educations_json = serializers.serialize("json", educations)
    return HttpResponse(educations_json, content_type="application/json")


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
    json_response = get_educations_json(request)

    educations = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )
    educations = [education.object for education in educations]
    title_query = request.GET.get("title", "").strip()

    context = {
        "name": "Andrew Chandra Halim",
        "education_list": educations,
        "title_query": title_query,
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