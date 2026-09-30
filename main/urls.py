from django.urls import path
from main.views import index, show_main, show_experience, show_education, show_projects, show_skills, create_Education, create_Experience, create_Projects, create_Skills, get_educations_json, get_experiences_json, get_skills_json, get_projects_json, delete_education, delete_experience, delete_projects, delete_skills, edit_projects, register, login_user, logout_user, toggle_starProject, toggle_starEducation, toggle_starSkills, toggle_starExperience, create_project_ajax

app_name = 'main'

urlpatterns = [
    # path('', index, name='index'),
    path("", show_main, name="show_main"),
    path("experience/", show_experience, name="show_experience"),
    path("education/", show_education, name="show_education"),
    path("projects/", show_projects, name="show_projects"),
    path("skills/", show_skills, name="show_skills"),
    #TUT 5
    path("projects/add-ajax/", create_project_ajax, name="create_project_ajax"),
    # TUGAS 4
    path("register/", register, name="register"),
    path("login/", login_user, name="login"),
    path("logout/", logout_user, name="logout"),
    path("projects/<uuid:project_id>/star/",toggle_starProject,name="toggle_starProject",),
    path("experience/<uuid:experience_id>/star/",toggle_starExperience,name="toggle_starExperience",),
    path("education/<uuid:education_id>/star/",toggle_starEducation,name="toggle_starEducation",),
    path("skills/<uuid:skills_id>/star/",toggle_starSkills,name="toggle_starSkills",),
    # TUGAS 3
    path("education/add/", create_Education, name="create_education"),
    path("experience/add/", create_Experience, name="create_experience"),
    path("skills/add/", create_Skills, name="create_skills"),
    path("projects/add/", create_Projects, name="create_projects"),
    path("api/projects/", get_projects_json, name="get_projects_json"),
    path("api/experiences/", get_experiences_json, name="get_experiences_json"),
    path("api/skills/", get_skills_json, name="get_skills_json"),
    path("api/educations/", get_educations_json, name="get_educations_json"),
    path("education/<uuid:education_id>/delete/" ,delete_education, name="delete_education"),
    path("experience/<uuid:experience_id>/delete/" ,delete_experience, name="delete_experience"),
    path("skill/<uuid:skills_id>/delete/" ,delete_skills, name="delete_skills"),
    path("projects/<uuid:projects_id>/delete/" ,delete_projects, name="delete_projects"),
    path("projects/<uuid:id>/edit/", edit_projects, name="edit_projects"),
    
]