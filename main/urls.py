from django.urls import path
from main.views import index, show_main, show_experience

app_name = 'main'

urlpatterns = [
    # path('', index, name='index'),
    path("", show_main, name="show_main"),
    path("experience/", show_experience, name="show_experience"),
]