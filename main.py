"""
Json oh yeah
"""

import json


def adjust_recipe(recipe, people):
    for i in recipe["ingredients"]:
        (recipe["ingredients"])[i] = recipe["ingredients"].get(i) / people
    recipe["servings"] -= people
    return recipe


def load_recipe(json_recipe):
    py_recipe = json.loads(json_recipe)
    return py_recipe


if __name__ == "__main__":
    # Beispiel für die Datenstruktur eines Rezepts
    recipe_json = '{"title": "Spaghetti Bolognese", "ingredients": {"Spaghetti": 400, "Tomato Sauce": 300, ' \
                  '"Minced Meat": 500}, "servings": 4} '
    adjust_recipe(load_recipe(recipe_json), 2)
    # Dein Code kommt hier hin
