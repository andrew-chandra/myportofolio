from django.forms import ModelForm, TextInput, Textarea, URLInput

from main.models import Education

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
