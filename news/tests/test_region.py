import pytest
from django.urls import reverse_lazy
from news.models import Region


@pytest.mark.django_db
def test_create_model_region():
    region = Region.objects.create(name='Tashkent')
    count = Region.objects.count()
    assert region.pk == 1
    assert region.name == 'Tashkent'
    assert count == 1


@pytest.mark.django_db
def test_create_region_api(client):
    url = reverse_lazy('region-list')
    data = {
        'name': 'Tashkent'
    }
    response = client.post(url, data)
    assert response.status_code == 201
    assert response.data['name'] == data['name']


@pytest.fixture
def regions():
    Region.objects.create(name='Toshkent')
    Region.objects.create(name='Navoi')


@pytest.mark.django_db
def test_region_list_api(client, regions):
    url = reverse_lazy('region-list')
    # url = '/api/v1/region/'
    response = client.get(url)
    assert response.status_code == 200
    assert len(response.data) == 2


@pytest.mark.django_db
def test_region_update_api(client, regions):
    region = Region.objects.first()
    '/api/v1/region/e09c9c1e-c071-4e4e-bc6f-76fc2b67d5f5/'
    url = reverse_lazy('region-detail', args=(region.pk, ))
    data = {
        'name': 'Fargona'
    }
    response = client.patch(url, data, content_type='application/json')
    assert response.status_code == 200
    assert response.data['name'] == data['name']
    assert response.data['id'] == region.pk
