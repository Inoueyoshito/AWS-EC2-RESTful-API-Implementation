from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import RecipeViewset

router = DefaultRouter()
router.register(r'recipes', RecipeViewset)

urlpatterns = [
    path('', include(router.urls))
]
