from django.urls import path
from .views import RecipeListCreate, RecipeDetail

urlpatterns = [
    path('', RecipeListCreate.as_view(), name='recipe_list_create'),
    path('<int:id>/', RecipeDetail.as_view(), name='recipe_detail'),
]

