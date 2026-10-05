from django.forms import ModelForm, TextInput, Textarea
from main.models import Education, Experience, Skills, Projects
from django.core.exceptions import ValidationError
from django.utils.html import strip_tags

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
    def clean_title(self):
        title = strip_tags(self.cleaned_data["title"]).strip()
        if not title:
            raise ValidationError("Nama pendidikan tidak boleh hanya berisi tag HTML.")
        return title

    def clean_description(self):
        return strip_tags(self.cleaned_data["description"]).strip()

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
    def clean_title(self):
        title = strip_tags(self.cleaned_data["title"]).strip()
        if not title:
            raise ValidationError("Nama proyek tidak boleh hanya berisi tag HTML.")
        return title

    def clean_description(self):
        return strip_tags(self.cleaned_data["description"]).strip()
    

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