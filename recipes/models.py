from django.db import models # type: ignore

#レシピ管理のモデル定義
class Recipe(models.Model):
    title = models.CharField(max_length=100)
    making_time = models.CharField(max_length=100)
    serves = models.CharField(max_length=100)
    ingredients = models.CharField(max_length=500)
    cost = models.CharField(max_length=10)

    def __str__(self):
        return self.title

