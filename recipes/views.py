from django.http import JsonResponse
from django.views import View
from .models import Recipe
from django.forms.models import model_to_dict
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

@method_decorator(csrf_exempt, name='dispatch')
class RecipeListCreate(View):
    def get(self, request):
        recipes = list(Recipe.objects.values())
        return JsonResponse({"recipes": recipes}, safe=False)
    
    def post(self, request):
        data = request.POST
        recipe = Recipe.objects.create(**data)
        return JsonResponse({"message": "レシピを正常に作成しました！", "recipe": model_to_dict(recipe)})

@method_decorator(csrf_exempt, name='dispatch')
class RecipeDetail(View):
    def get(self, request, id):
        recipe = Recipe.objects.filter(id=id).first()
        if recipe:
            return JsonResponse({"message": "IDによるレシピ詳細", "recipe": model_to_dict(recipe)})
        else:
            return JsonResponse({"message": "レシピが見つかりません"}, status=404)
    
    def patch(self, request, id):
        data = request.POST
        Recipe.objects.filter(id=id).update(**data)
        recipe = Recipe.objects.get(id=id)
        return JsonResponse({"message": "レシピを正常に更新しました！", "recipe": model_to_dict(recipe)})
    
    def delete(self, request, id):
        count, _ = Recipe.objects.filter(id=id).delete()
        if count:
            return JsonResponse({"message": "レシピを正常に削除しました！"})
        else:
            return JsonResponse({"message": "レシピが見つかりません"}, status=404)
