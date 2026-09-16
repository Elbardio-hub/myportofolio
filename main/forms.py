from django.forms import ModelForm, TextInput, Textarea, URLInput, Select, DateInput
from main.models import Experience

class ExperienceForm(ModelForm):
    class Meta:
        model = Experience
        fields = [
            "title",
            "category",
            "description",
            "thumbnail",
            "ended_at",
        ]

        labels = {
            "title": "Judul Posisi / Peran",
            "category": "Kategori Pengalaman",
            "description": "Deskripsi Pekerjaan / Tanggung Jawab",
            "thumbnail": "Dokumentasi",
            "ended_at": "Tanggal Selesai (Kosongkan jika masih berlangsung)",
        }

        widgets = {
            "title": TextInput(
                attrs={
                    "placeholder": "Software Engineer Intern",
                    "maxlength": 255,
                }
            ),
            "category": Select(
                attrs={
                    "class": "form-select",
                }
            ),
            "description": Textarea(
                attrs={
                    "placeholder": "Jelaskan tanggung jawab dan pencapaian selama pengalaman ini...",
                    "rows": 3,
                }
            ),
            "thumbnail": URLInput(
                attrs={
                    "placeholder": "https://example.com/image.png",
                }
            ),
            "ended_at": DateInput(
                attrs={
                    "type": "date",
                }
            ),
        }