# Functions/classes available to all modules

class FoodPages:
    def __init__(self, recipes, wikisum):
        self.wikisum = wikisum
        self.recipes = recipes

    def __str__(self):
        return f"""Wikipedia summary: {self.wikisum}
        Recipes: {self.recipes}"""

# For debugging large strings
def writeText(txt):
    with open('a.txt', 'w') as f:
        f.write(txt)