import pytest
from model_bakery import baker
from rest_framework.test import APIClient
from students.models import Course, Student


# Заведите фикстуры:
# для api-client'а
@pytest.fixture
def client():
    return APIClient()


# для фабрики курсов
@pytest.fixture
def courses_factory():
    def factory(*args, **kwargs):
        return baker.make(Course, *args, **kwargs)

    return factory


# для фабрики студентов
@pytest.fixture
def students_factory():
    def factory(*args, **kwargs):
        return baker.make(Student, *args, **kwargs)

    return factory


# проверка получения 1го курса (retrieve-логика)
@pytest.mark.django_db
def test_create_get_course(client, courses_factory):
    course = courses_factory(_quantity=1)
    check_course = course[0]
    response = client.get(f'/api/v1/courses/{check_course.id}/')
    assert response.status_code == 200

    data = response.json()
    assert data['name'] == check_course.name


# проверка получения списка курсов (list-логика)
@pytest.mark.django_db
def test_create_get_courses(client, courses_factory):
    courses = courses_factory(_quantity=10)
    response = client.get('/api/v1/courses/')
    assert response.status_code == 200

    data = response.json()
    for i, item in enumerate(data):
        assert item['name'] == courses[i].name


# проверка фильтрации списка курсов по id
@pytest.mark.django_db
def test_filter_course_by_id(client, courses_factory):
    course = courses_factory(_quantity=10)
    response = client.get('/api/v1/courses/', {'id': course[0].id})
    assert response.status_code == 200

    data = response.json()
    assert course[0].id == data[0]['id']


# проверка фильтрации списка курсов по name
@pytest.mark.django_db
def test_filter_course_by_name(client, courses_factory):
    course = courses_factory(_quantity=5)
    response = client.get('/api/v1/courses/', {'name': course[0].name})
    assert response.status_code == 200

    data = response.json()
    assert course[0].name == data[0]['name']


# тест успешного создания курса
@pytest.mark.django_db
def test_create_course(client):
    response = client.post('/api/v1/courses/', data={'name': 'Django-backend'}, format='json')
    assert response.status_code == 201

    data = response.json()
    assert Course.objects.get(id=data['id']).name == 'Django-backend'


# тест успешного обновления курса
@pytest.mark.django_db
def test_update_course(client, courses_factory):
    course = courses_factory(_quantity=5)
    response = client.patch(f'/api/v1/courses/{course[2].id}/', data={'name': 'test-name'}, format='json')
    assert response.status_code == 200

    data = response.json()
    assert data['name'] == 'test-name'


# тест успешного удаления курса
@pytest.mark.django_db
def test_delete_course(client, courses_factory):
    course = courses_factory(_quantity=1)
    response = client.delete(f'/api/v1/courses/{course[0].id}/')
    assert response.status_code == 204
