# Problem: 2115. Find All Possible Recipes from Given Supplies - https://leetcode.com/problems/find-all-possible-recipes-from-given-supplies/description/

from collections import deque
class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        ingredient_to_recipes = {}
        in_degree = {}
        recipe_set = set(recipes)
        
        for i, recipe in enumerate(recipes):
            in_degree[recipe] = len(ingredients[i])  
            for ing in ingredients[i]:
                if ing not in ingredient_to_recipes:
                    ingredient_to_recipes[ing] = []
                ingredient_to_recipes[ing].append(recipe)

        queue = deque(supplies)  
        result = []

        while queue:
            ingredient = queue.popleft()

            if ingredient in recipe_set:
                result.append(ingredient)

            for recipe in ingredient_to_recipes.get(ingredient, []):
                in_degree[recipe] -= 1
                if in_degree[recipe] == 0:
                    queue.append(recipe)

        return result