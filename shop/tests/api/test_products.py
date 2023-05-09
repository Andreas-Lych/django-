import pytest
from rest_framework.test import APIClient
from products.models import Product
from tests.factories import ProductFactory


@pytest.mark.django_db
class TestProductApi:
    def setup_method(self):
        self.client = APIClient()

    def test_index(self):
        response = self.client.get("/api/products/")
        assert response.status_code == 200
        assert len(response.json()) == 0

        response = self.client.post("/api/products/", data={
            "title": "BMW",
            "color": "WHITE",
            "price": 275,
        })
        assert response.status_code == 201
        assert Product.objects.exists()

    def test_delete_product(self):
        product = Product.objects.create(title="BMW", color="WHITE", price=275)

        response = self.client.get(f"/api/products/{product.id}/")
        assert response.status_code == 200
        assert response.json()["title"] == "BMW"

        response = self.client.delete(f"/api/products/{product.id}/")
        assert response.status_code == 204
        assert not Product.objects.exists()

    def test_popular(self):
        ProductFactory.create_batch(10)
        response = self.client.get("/api/products/popular/")

        assert response.status_code == 200
        assert response.json().get("count") == 10

