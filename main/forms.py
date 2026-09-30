from django.forms import ModelForm, TextInput, Textarea
from main.models import Education, Experience, Skills, Projects

class EducationForm(ModelForm):
    class Meta:
        model = Education
        fields = [
            "title",
            "description",
            "kesan",
            # "thumbnail",
            # "started_at",
            # "ended_at",
        ]

        labels = {
            "title": "Sekolah / Kampus",
            "description": "Deskripsi",
            "kesan": "Kesan selama belajar",
        }

        widgets = {
            "title": TextInput(
                attrs={
                    "placeholder": "Sekolah",
                    "maxlength": 255,
                }
            ),
            "description": Textarea(
                attrs={
                    "placeholder": "Deskripsikan",
                    "rows": 3,
                }
            ),
            "kesan": Textarea(
                attrs={
                    "placeholder": "Kesanmu",
                    "rows": 2,
                }
            )
        }

class ExperienceForm(ModelForm):
    class Meta:
        model = Experience
        fields = [
            "title",
            "description",
            "category",
            # "thumbnail",
            # "started_at",
            # "ended_at",
        ]

        labels = {
            "title": "Pengalaman",
            "description": "Deskripsi",
            "category": "Kategori",
        }

        widgets = {
            "title": TextInput(
                attrs={
                    "placeholder": "Pengalaman",
                    "maxlength": 255,
                }
            ),
            "description": Textarea(
                attrs={
                    "placeholder": "Deskripsikan",
                    "rows": 3,
                }
            ),
            "category": Textarea(
                attrs={
                    "placeholder": "Jenis",
                    "rows": 2,
                }
            )
        }

class ProjectForm(ModelForm):
    class Meta:
        model = Projects
        fields = [
            "title",
            "description",
            "category",
            # "thumbnail",
            # "started_at",
            # "ended_at",
        ]

        labels = {
            "title": "Proyek",
            "description": "Deskripsi",
            "category": "Kategori",
        }

        widgets = {
            "title": TextInput(
                attrs={
                    "placeholder": "Proyek",
                    "maxlength": 255,
                }
            ),
            "description": Textarea(
                attrs={
                    "placeholder": "Deskripsikan",
                    "rows": 3,
                }
            ),
            "category": Textarea(
                attrs={
                    "placeholder": "Jenis",
                    "rows": 2,
                }
            )
        }

class SkillsForm(ModelForm):
    class Meta:
        model = Skills
        fields = [
            "title",
            "description",
            "category",
            # "thumbnail",
            # "started_at",
            # "ended_at",
        ]

        labels = {
            "title": "Keahlian",
            "description": "Deskripsi",
            "category": "Kategori",
        }

        widgets = {
            "title": TextInput(
                attrs={
                    "placeholder": "Keahlian",
                    "maxlength": 255,
                }
            ),
            "description": Textarea(
                attrs={
                    "placeholder": "Deskripsikan",
                    "rows": 3,
                }
            ),
            "category": Textarea(
                attrs={
                    "placeholder": "Jenis",
                    "rows": 2,
                }
            )
        }