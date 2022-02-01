from urllib.parse import urlparse

from django.urls import path,include
from .views import *
from rest_framework.routers import SimpleRouter
# Create your tests here.
router = SimpleRouter()
router.register("students",StudentApiView,basename="student_api")

urlpatterns = [
    path("",StudentView.as_view(),name="student"),
    path("<int:id>/",StudentDetailView.as_view(),name="student_detail"),
    path("<int:id>/delete/",delete_student,name="student_delete"),
    path("api/v1/",include(router.urls)),

]
