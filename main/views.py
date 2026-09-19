from django.shortcuts import render
from main.models import Experience, Education
from django.contrib import messages
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect
from main.forms import ExperienceForm, EducationForm
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
    json_response = get_experience_json(request)

    experiences = serializers.deserialize(
        "json",
        json_response.content.decode("UTF-8")
    )

    experiences = [experience.object for experience in experiences]
    title_query = request.GET.get("title", "").strip()

    context = {
        "name": "Ardi",
        "experience_list": experiences,
        "title_query": title_query,
    }
    return render(request, "experience.html", context)
    

def show_education(request):
    json_response = get_education_json(request)

    educations = serializers.deserialize(
        "json",
        json_response.content.decode("UTF-8")
    )

    educations = [education.object for education in educations]
    school_query = request.GET.get("school", "").strip()

    context = {
        "name": "Ardi",
        "education_list": educations,
        "school_query": school_query,
    }
    return render(request, "education.html", context)




def create_experience(request):
    form = ExperienceForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Experience baru berhasil ditambahkan")
        return redirect("main:show_experience")
    context = {
        "name": "Ardi",
        "form": form,
    }

    return render(request, "experience_form.html", context)

def get_experience_json(request):
    title_query = request.GET.get("title", "").strip()
    experience = Experience.objects.all()

    if title_query:
        experience = experience.filter(title__icontains=title_query)

    experience_json = serializers.serialize("json", experience)
    return HttpResponse(experience_json, content_type="application/json")

def delete_experience(request, experience_id):
    experience = get_object_or_404(Experience, pk=experience_id)

    if request.method == "POST":
        experience.delete()
        messages.success(request, "Experience berhasil dihapus!")
        return redirect("main:show_experience")

    return redirect("main:show_experience")

def create_education(request):
    form = EducationForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Riwayat Pendidikan baru berhasil ditambahkan!")
        return redirect("main:show_education")

    context = {
        "name": "Ardi",
        "form": form,
    }
    return render(request, "education_form.html", context)

def get_education_json(request):
    school_query = request.GET.get("school", "").strip()
    education = Education.objects.all().order_by("-started_year")

    if school_query:
        education = education.filter(school__icontains=school_query)

    education_json = serializers.serialize("json", education)
    return HttpResponse(education_json, content_type="application/json")

def edit_education(request, education_id):
    education = get_object_or_404(Education, pk=education_id)
    form = EducationForm(request.POST or None, instance=education)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Riwayat pendidikan berhasil diperbarui!")
        return redirect("main:show_education")

    context = {
        "name": "Ardi",
        "form": form,
        "education": education,
    }

    return render(request, "education_edit_form.html", context)

def delete_education(request, education_id):
    education = get_object_or_404(Education, pk=education_id)
    if request.method == "POST":
        education.delete()
        messages.success(request, "Riwayat pendidikan berhasil dihapus!")
        return redirect("main:show_education")
    return redirect("main:show_education")


