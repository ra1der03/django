import pytest
from rest_framework.test import APIClient
from model_bakery import baker
import json

from students.models import Student, Course


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def student_factory():
    def factory(*args, **kwargs):
        return baker.make(Student, _fill_optional=['birth_date'], *args, **kwargs)
    return factory


@pytest.fixture
def course_factory():
    def factory(*args, **kwargs):
        return baker.make(Course,  *args, **kwargs)
    return factory


@pytest.mark.django_db
def test_cources(client, student_factory, course_factory):
    students = student_factory(_quantity=2)
    courses = course_factory(_quantity=2)
    for i, student in enumerate(students):
        client.post('/students/', data={'student_name': student.student_name, 'birth_date': '2003-05-03'})
        for course in courses:
            client.post('/courses/', data={'name': course.name, 'students_id': i})
    response = client.get('/courses/1/')
    assert response.status_code == 200


@pytest.mark.django_db
def test_list(client, student_factory, course_factory):
    students = student_factory(_quantity=2)
    courses = course_factory(_quantity=2)
    response = client.get('/courses/')
    assert response.status_code == 200


@pytest.mark.django_db
def test_full(client, student_factory, course_factory):
    students = student_factory(_quantity=2)
    courses = course_factory(_quantity=2)
    response = client.get('/courses/')
    data = response.json()
    assert len(data) == len(courses)


@pytest.mark.django_db
def test_id(client, student_factory, course_factory):
    students = student_factory(_quantity=2)
    courses = course_factory(_quantity=2)
    response = client.get('/courses/', {'id': courses[1].id})
    data = response.json()
    assert data[0]['id'] == courses[1].id


@pytest.mark.django_db
def test_name(client, student_factory, course_factory):
    students = student_factory(_quantity=2)
    courses = course_factory(_quantity=2)
    response = client.get('/courses/', {'name': courses[1].name}, headers={"accept": "application/json"})
    data = response.json()
    assert data[0]['name'] == courses[1].name


@pytest.mark.django_db
def test_create(client, student_factory, course_factory):
    students = student_factory(_quantity=2)
    students_id = [i.id for i in students]
    response = client.post('/courses/',
                data={'name': 'Ffjjhiufy', 'students': students_id}, headers={"accept": "application/json"})
    assert response.status_code == 201


@pytest.mark.django_db
def test_update(client, student_factory, course_factory):
    students = student_factory(_quantity=2)
    courses = course_factory(_quantity=2)
    course_id = courses[0].id
    url = f"/courses/{course_id}/"
    response = client.patch(url, data={'name': 'django-new', 'students': students[0].id})
    assert response.status_code == 200


@pytest.mark.django_db
def test_remove(client, student_factory, course_factory):
    students = student_factory(_quantity=2)
    courses = course_factory(_quantity=2)
    course_id = courses[0].id
    url = f"/courses/{course_id}/"
    response = client.delete(url)
    assert response.status_code == 204

