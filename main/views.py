from django.shortcuts import render
from .models import Mahasiswa
from .models import Experience

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