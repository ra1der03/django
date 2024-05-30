import pytest
from rest_framework.test import APIClient
from model_bakery import baker

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
    for student in students:
        client.post('/students/', data={'student_name': student.student_name, 'birth_date': '2003-05-03'})
        for course in courses:
            client.post('/courses/', data={'name': course.name, 'students_id': '1'})

    response = client.get('/courses/1/')
    assert response.status_code == 200

    response = client.get('/courses/')
    assert response.status_code == 200

    data = response.json()
    assert len(data) == len(courses)

    response = client.get('/courses/?id=2')
    data = response.json()
    assert data[0]['id'] == 2

    response = client.get('/courses/?name='+courses[1].name)
    data = response.json()
    assert data[0]['name'] == courses[1].name

    response = client.post('/courses/', data={'name': 'DJANGO', 'students': [1, 2]})
    assert response.status_code == 201

    response = client.patch('/courses/3/', data={'name': 'django-new', 'students': [1, 2]})
    assert response.status_code == 200

    response = client.delete('/courses/3/')
    assert response.status_code == 204
