from django.forms import ModelForm, TextInput, Textarea, URLInput, Select, DateInput, NumberInput
from main.models import Experience, Education

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

class EducationForm(ModelForm):
    class Meta:
        model = Education
        fields = [
            "school",
            "degree",
            "started_year",
            "ended_year",
            "description",
        ]

        labels = {
            "school": "Nama Sekolah / Institusi",
            "degree": "Jenjang / Jurusan",
            "started_year": "Tahun Mulai",
            "ended_year": "Tahun Selesai (Kosongkan jika msaih berlangsung)",
            "description": "Deskripsi",
        }

        widgets = {
            "school": TextInput(
                attrs={
                    "placeholder": "Contoh: Universitas Indonesia"
                }
            ),
            "degree": TextInput(
                attrs={
                    "placeholder": "Contoh: S1 Ilmu Komputer"
                }
            ),
            "started_year": NumberInput(
                attrs={
                    "placeholder": "2024"
                }
            ),
            "ended_year": NumberInput(
                attrs={
                    "placeholder": "Kosongkan jika masih memnpuh pendidikan"
                }
            ),
            "descrition": Textarea(
                attrs={
                    "rows": 4,
                    "placeholder": "Fokus pembelajaran, pencapaian, atau kegiatan akademis...",
                }
            ),
        }
