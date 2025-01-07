from openai import OpenAI
from globals import *
MODEL = "gpt-4o-mini"

client = OpenAI()


# Generic function to get ChatGPT response
def askGPT(sys_prompt, user_prompt):
    completion = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": sys_prompt},
            {
                "role": "user",
                "content": user_prompt
            }
        ]
    )

    return completion.choices[0].message.content

# Given the text of a recipe website page, summarize it with ChatGPT
def summarizeRecipe(page, food):
    return askGPT(f"""You will be given a web page from a recipe web site for a {food} recipe. 
        Do the following:
        Summarize any information in the web site about the food being prepared.
        (Ignore any irrelevant information such as personal details about the writer,
        or claims about how good the recipe is).
        Then, give the recipe by itself (ingredients and steps).
        Only give me the information I asked for, do not say anything else.
        If the web page you receive is an error or contains no recipe, just say '(No recipe)'""",
        page)

# Summarize all recipes in the FoodPages object with ChatGPT
def summarizePages(foodpages, food):
    summ_recipes = [summarizeRecipe(page, food) for page in foodpages.recipes]
    return FoodPages(summ_recipes, foodpages.wikisum)

# Combine all summarized information and give a final summary with ChatGPT
def finalSummary(foodpages, food):
    recipe_strs = [f"Recipe {recipe_index[0]}: {recipe_index[1]}"
                  for recipe_index in enumerate(foodpages.recipes)]
    recipe_str = "\n".join(recipe_strs)

    if foodpages.wikisum is None:
        user_prompt = recipe_str
    else:
        user_prompt = f"Summary: {foodpages.wikisum}\n" + recipe_str
    return askGPT(f"""You will receive some information and recipes about {food}.
        Combine all into a total summary of {food}. Include the following:
        - The main ingredients of {food} and how it's prepared
        - Additional ingredients that are used in some of the recipes
        - Any other information given to you, if it's important
        - Existence of options for alternative diets (e.g. vegetarian/vegan/gluten-free) if it's relevant and provided to you
        Do not include the following:
        - History, origins, or culture of the dish
        - Any 'fluff' that does not convey useful information (e.g. 'lasagna remains a beloved dish for many')""",
        user_prompt
    )
