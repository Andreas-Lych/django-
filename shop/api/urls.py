from django.urls import include, path
from rest_framework import routers
from api.products.views import ProductViewSet
from api.feedback.views import FeedbackViewSet
from api.users.views import RegisterView
from api.users.views import LoginView


app_name = "api"

router = routers.DefaultRouter()
router.register(r"products", ProductViewSet)
router.register(r"feedback", FeedbackViewSet)


urlpatterns = [
    path("", include(router.urls)),
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
]