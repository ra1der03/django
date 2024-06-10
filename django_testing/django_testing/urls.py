"""django_testing URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

<<<<<<< HEAD
from students.views import CoursesViewSet, StudentViewSet

router = DefaultRouter()
router.register("courses", CoursesViewSet, basename="courses")
router.register("students", StudentViewSet, basename="students")
router.register('courses/<pk>/', CoursesViewSet)
=======
from students.views import CoursesViewSet

router = DefaultRouter()
router.register("courses", CoursesViewSet, basename="courses")
# router.register('courses/<pk>/', CoursesViewSet)
>>>>>>> b384975f6822368497afa684c0352ef1ae7dae6e

urlpatterns = [
    path('admin/', admin.site.urls),
] + router.urls
