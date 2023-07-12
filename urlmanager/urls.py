from django.urls import path
from django.views.generic import TemplateView

from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', views.URLView, basename='urls')

urlpatterns = router.urls
