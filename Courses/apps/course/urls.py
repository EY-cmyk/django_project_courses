from django.urls import path
from . import views

app_name = 'courses'

urlpatterns = [
path('', views.index, name = 'index'),
path('<int:course_id>/', views.courseview, name = 'courseview'),
]
