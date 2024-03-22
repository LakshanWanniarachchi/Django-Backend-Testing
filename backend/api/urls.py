from django.urls import path
from .views import studentview , studentData


urlpatterns = [
    path('student',studentview.as_view() ),
    path('all-data',studentData.as_view() ),
]
