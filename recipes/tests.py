from django.urls import reverse # type: ignore
from rest_framework.test import APITestCase, APIClient # type: ignore
from rest_framework import status # type: ignore
from .models import Recipe

class RecipeTestCase(APITestCase):
    def setUp(self):
        # テスト用のレシピを事前に作成
        self.recipe = Recipe.objects.create(
            title="Test Recipe",
            making_time="15 minutes",
            serves="1 person",
            ingredients="Eggs, Salt",
            cost="200"
        )

    def test_create_recipe(self):
        """
        新しいレシピの作成をテスト
        """
        url = reverse('recipe-list')
        data = {
            "title": "Omelette",
            "making_time": "10 minutes",
            "serves": "1 person",
            "ingredients": "Eggs, Salt, Pepper",
            "cost": "100"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Recipe.objects.count(), 2)  # 新しいレシピが追加されたか確認

    def test_get_recipes(self):
        """
        レシピ一覧の取得をテスト
        """
        url = reverse('recipe-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # setUpで作成したレシピが存在することを確認

    def test_update_recipe(self):
        """
        レシピの更新をテスト
        """
        url = reverse('recipe-detail', args=[self.recipe.id])
        data = {
            "title": "Updated Recipe"
        }
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.recipe.refresh_from_db()
        self.assertEqual(self.recipe.title, "Updated Recipe")  # タイトルが更新されたか確認

    def test_delete_recipe(self):
        """
        レシピの削除をテスト
        """
        url = reverse('recipe-detail', args=[self.recipe.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Recipe.objects.count(), 0)  # レシピが削除されたか確認
