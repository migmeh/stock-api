# test_api.py
import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from api.models import Producto, Orden

@pytest.mark.sanity
def test_me():
    """I'm a test."""

    assert True

@pytest.fixture
def client():
    return APIClient()

@pytest.fixture
def new_product(db):
    return Producto.objects.create(sku="TEST123", name="Test Product")

@pytest.mark.django_db
def test_create_product(client):
    url = reverse('create_product')
    data = {'sku': 'TEST123', 'name': 'Test Product'}
    response = client.post(url, data, format='json')
    assert response.status_code == status.HTTP_201_CREATED
    assert Producto.objects.filter(sku='TEST123').exists()

@pytest.mark.django_db
def test_update_inventory(client, new_product):
    url = reverse('update_inventory', kwargs={'pk': new_product.id})
    data = {'stock': 50}
    response = client.patch(url, data, format='json')
    assert response.status_code == status.HTTP_200_OK
    new_product.refresh_from_db()
    assert new_product.stock == 150

@pytest.mark.django_db
def test_create_order(client, new_product):
    url = reverse('create_order')
    data = {
        'productos': [
            {
                'id': new_product.id,
                'cantidad': 1
            }
        ]
    }
    response = client.post(url, data, format='json')
    assert response.status_code == status.HTTP_201_CREATED
    assert Orden.objects.count() == 1
    assert Orden.objects.first().productos.filter(id=new_product.id).exists()
