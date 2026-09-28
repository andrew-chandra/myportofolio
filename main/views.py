import datetime
from .models import Mahasiswa
from .models import Experience
from .models import Education
from .models import Skills
from .models import Projects
from .forms import EducationForm, ExperienceForm, ProjectsForm, SkillsForm
from django.contrib import messages
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required 
from django.core.exceptions import PermissionDenied        


##TUGAS 4
def get_educations_json(request):
    title_query = request.GET.get("title", "").strip()
    educations = Education.objects.all()

    if title_query:
        educations = educations.filter(description__icontains=title_query)

    educations_json = serializers.serialize("json", educations, use_natural_foreign_keys=True)
    return HttpResponse(educations_json, content_type="application/json")

def get_experiences_json(request):
    title_query = request.GET.get("title", "").strip()
    experiences = Experience.objects.all()

    if title_query:
        experiences = experiences.filter(title__icontains=title_query)

    experiences_json = serializers.serialize("json", experiences, use_natural_foreign_keys=True)
    return HttpResponse(experiences_json, content_type="application/json")

def get_skills_json(request):
    title_query = request.GET.get("title", "").strip()
    skills = Skills.objects.all()

    if title_query:
        skills = skills.filter(title__icontains=title_query)

    skills_json = serializers.serialize("json", skills, use_natural_foreign_keys=True)
    return HttpResponse(skills_json, content_type="application/json")

def get_projects_json(request):
    title_query = request.GET.get("title", "").strip()
    projects = Projects.objects.all()

    if title_query:
        projects = projects.filter(title__icontains=title_query)

    # projects_json = serializers.serialize("json", projects) sebelum
    projects_json = serializers.serialize("json", projects, use_natural_foreign_keys=True)  # sesudah
    return HttpResponse(projects_json, content_type="application/json")

@login_required(login_url="/login/")
def toggle_starEducation(request, education_id):
    education = get_object_or_404(Education, pk=education_id)

    if request.method == "POST":
        # Kalau akun ini sudah pernah memberi star, batalkan star-nya.
        # Kalau belum, tambahkan star.
        if request.user in education.starred_by.all():
            education.starred_by.remove(request.user)
        else:
            education.starred_by.add(request.user)

    return redirect("main:show_education")

@login_required(login_url="/login/")
def toggle_starExperience(request, experience_id):
    experience = get_object_or_404(Experience, pk=experience_id)

    if request.method == "POST":
        # Kalau akun ini sudah pernah memberi star, batalkan star-nya.
        # Kalau belum, tambahkan star.
        if request.user in experience.starred_by.all():
            experience.starred_by.remove(request.user)
        else:
            experience.starred_by.add(request.user)

    return redirect("main:show_experience")

@login_required(login_url="/login/")
def toggle_starSkills(request, skills_id):
    skill = get_object_or_404(Skills, pk=skills_id)

    if request.method == "POST":
        # Kalau akun ini sudah pernah memberi star, batalkan star-nya.
        # Kalau belum, tambahkan star.
        if request.user in skill.starred_by.all():
            skill.starred_by.remove(request.user)
        else:
            skill.starred_by.add(request.user)

    return redirect("main:show_skills")

##TUTOR 4
# Tanpa cek is_superuser: semua akun yang sudah login boleh memberi star
@login_required(login_url="/login/")
def toggle_starProject(request, project_id):
    project = get_object_or_404(Projects, pk=project_id)

    if request.method == "POST":
        # Kalau akun ini sudah pernah memberi star, batalkan star-nya.
        # Kalau belum, tambahkan star.
        if request.user in project.starred_by.all():
            project.starred_by.remove(request.user)
        else:
            project.starred_by.add(request.user)

    return redirect("main:show_projects")

def show_main(request):
    last_login = request.COOKIES.get('last_login', 'Belum ada sesi login / Cookie tidak ditemukan')
    context = {
        "name": "Andrew Chandra Halim",
        "npm": "2506656431",
        "study_program": "S1 Ilmu Komputer",
        "bio": (
            "Mahasiswa Ilmu Komputer Universitas Indonesia yang tertarik "
            "pada pengembangan perangkat lunak dan pendidikan."
        ),
        "last_login": last_login,
    }
    return render(request, "index.html", context)

def register(request):
    form = UserCreationForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Akun berhasil dibuat. Silakan login.")
        return redirect("main:login")

    context = {
        "name": "Andrew Chandra Halim",
        "form": form,
    }
    return render(request, "register.html", context)

def login_user(request):
    form = AuthenticationForm(request, data=request.POST or None)

    if request.method == "POST" and form.is_valid():
        user = form.get_user()
        login(request, user)
        response = redirect("main:show_main")
        response.set_cookie('last_login', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        return response

    context = {
        "name": "Andrew Chandra Halim",
        "form": form,
    }
    return render(request, "login.html", context)

def logout_user(request):
    logout(request)
    response = redirect("main:show_main")
    response.delete_cookie('last_login')
    return response

### tambahin login required untuk membatasi hak (hanya user dari django admin yang bisa)
@login_required(login_url="/login/")
def create_Education(request):
    if not request.user.is_superuser:
        raise PermissionDenied
    
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

@login_required(login_url="/login/")
def create_Experience(request):
    if not request.user.is_superuser:
        raise PermissionDenied
        
    form = ExperienceForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Data baru berhasil ditambahkan!")
        return redirect("main:show_experience")
    
    context = {
        "name": "Andrew Chandra Halim",
        "form": form,
    }
    return render(request, "experience_form.html", context)

@login_required(login_url="/login/")
def create_Skills(request):
    if not request.user.is_superuser:
        raise PermissionDenied
        
    form = SkillsForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Data baru berhasil ditambahkan!")
        return redirect("main:show_skills")
    
    context = {
        "name": "Andrew Chandra Halim",
        "form": form,
    }
    return render(request, "skills_form.html", context)

@login_required(login_url="/login/")
def create_Projects(request):
    if not request.user.is_superuser:
        raise PermissionDenied
        
    form = ProjectsForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Data baru berhasil ditambahkan!")
        return redirect("main:show_projects")
    
    context = {
        "name": "Andrew Chandra Halim",
        "form": form,
    }
    return render(request, "projects_form.html", context)

@login_required(login_url="/login/")
def delete_education(request, education_id):
    if not request.user.is_superuser:
        raise PermissionDenied
        
    education = get_object_or_404(Education, pk=education_id)

    if request.method == "POST":
        education.delete()
        messages.success(request, "Education berhasil dihapus!")
        return redirect("main:show_education")

    return redirect("main:show_education")

@login_required(login_url="/login/")
def delete_experience(request, experience_id):
    if not request.user.is_superuser:
        raise PermissionDenied
        
    experience = get_object_or_404(Experience, pk=experience_id)

    if request.method == "POST":
        experience.delete()
        messages.success(request, "Experience berhasil dihapus!")
        return redirect("main:show_experience")

    return redirect("main:show_experience")

@login_required(login_url="/login/")
def delete_skills(request, skills_id):
    if not request.user.is_superuser:
        raise PermissionDenied
        
    skills = get_object_or_404(Skills, pk=skills_id)

    if request.method == "POST":
        skills.delete()
        messages.success(request, "Skill berhasil dihapus!")
        return redirect("main:show_skills")

    return redirect("main:show_skills")

@login_required(login_url="/login/")
def delete_projects(request, projects_id):
    if not request.user.is_superuser:
        raise PermissionDenied
        
    projects = get_object_or_404(Projects, pk=projects_id)

    if request.method == "POST":
        projects.delete()
        messages.success(request, "Projects berhasil dihapus!")
        return redirect("main:show_projects")

    return redirect("main:show_projects")

def index(request):
    mahasiswas = Mahasiswa.objects.all()

    context = {'mahasiswas' : mahasiswas}

    return render(request, 'index.html', context)



def show_experience(request):
    json_response = get_experiences_json(request)

    experiences = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )
    experiences = [experience.object for experience in experiences]
    title_query = request.GET.get("title", "").strip()
    context = {
        "name": "Andrew Chandra Halim",
        "experience_list": experiences,
        "title_query": title_query,
    }
    return render(request, "experience.html", context)

## EDIT UNTUK SEARCH
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
    json_response = get_skills_json(request)

    skills = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )
    skills = [skill.object for skill in skills]
    title_query = request.GET.get("title", "").strip()

    context = {
        "name": "Andrew Chandra Halim",
        "skills_list": skills,
        "title_query": title_query,
    }
    return render(request, "skills.html", context)

def show_projects(request):
    json_response = get_projects_json(request)

    projects = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )
    projects = [project.object for project in projects]
    title_query = request.GET.get("title", "").strip()
    context = {
        "name": "Andrew Chandra Halim",
        "projects_list": projects,
        "title_query": title_query,
    }
    return render(request, "projects.html", context)

def edit_projects(request, id):
    project = get_object_or_404(Projects, pk=id)

    form = ProjectsForm(request.POST or None, instance=project)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Proyek berhasil diperbarui!")
        return redirect("main:show_projects")

    context = {
        "name": "Andrew Chandra Halim",
        "form": form,
        "project": project,
    }
    return render(request, "edit_projects.html", context)