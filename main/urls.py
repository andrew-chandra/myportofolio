from django.urls import path
from main.views import index, show_main, show_experience, show_education, show_projects, show_skills, create_Education, get_educations_json, delete_education

app_name = 'main'

urlpatterns = [
    # path('', index, name='index'),
    path("", show_main, name="show_main"),
    path("experience/", show_experience, name="show_experience"),
    path("education/", show_education, name="show_education"),
    path("projects/", show_projects, name="show_projects"),
    path("skills/", show_skills, name="show_skills"),
    path("education/add/", create_Education, name="create_education"),
    path("api/educations/", get_educations_json, name="get_educations_json"),
    path("education/<uuid:education_id>/delete/" ,delete_education, name="delete_education"),
    
]