from django.shortcuts import render
from main.models import Experience, Education
# Create your views here.

def show_main(request):
    context = {
        "name": "Ardi",
        "npm": "2506547203",
        "study_program": "S1 Ilmu Komputer",
        "bio": (
            "Mahasiswa Ilmu Komputer Universitas Indonesia yang tertarik "
            "pada pengembangan perangkat lunak dan pendidikan."
        ),
    }
    return render(request, "index.html", context)

def show_experience(request):
    context = {
        "name": "Ardi",
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)

def show_education(request):
    education_list = Education.objects.all().order_by('-started_year')
    context = {
        "name": "Ardi",
        "education_list": education_list,
    }
    return render(request, "education.html", context)