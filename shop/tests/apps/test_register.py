import pytest
from django.contrib.auth.models import User
from django.test.client import Client


@pytest.mark.django_db
class TestRegister:
    def setup_method(self):
        self.client = Client()

    def test_register(self):
        response = self.client.get("/register/")
        assert response.status_code == 200

        responce = self.client.post("/register/", data={
            "email": "test@test.com",
            "password": "test@test.com",
            "first_name": "Test",
            "last_name": "Test",
        }, follow=True)
        assert responce.status_code == 200
        assert User.objects.exists()