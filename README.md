# GPTFoodSummarizer
This program is inspired by my personal use of ChatGPT. I would often use it in cooking - not for recipes, but to get inspiration and ask questions about dishes. Trying to get detailed information overall about a dish, such as the main ingredients and preparation, is difficult on any normal web search because it involves comparing multiple recipes, each of which will have individual quirks, to get the main idea. GPTFoodSummarizer will do this automatically, pulling multiple recipes from Google and providing an overall summary, while also incorporating information from the food's Wikipedia article if available.

## Usage:
An OpenAI API key is required to use this program.

```bash
$ export OPENAI_API_KEY=<openai key>
$ python main.py <foodname>
```

foodname must be wrapped in quotes if it is made of multiple words, e.g. "lentil soup"

## Example Output:
```bash
$ python main.py lasagna
```

**Lasagna Summary**

Lasagna is a layered pasta dish typically prepared with wide, flat sheets of pasta, combined with various fillings and sauces. The main ingredients commonly include:

- **Pasta:** Lasagna noodles, either dried or fresh.
- **Meat Sauce (Ragù):** This often consists of ground beef or sausage, garlic, onions, and tomatoes (either crushed tomatoes or tomato paste), seasoned with herbs and spices like basil, parsley, and oregano.
- **Cheese:** A combination of cheeses is used, commonly ricotta, cottage cheese, mozzarella, and Parmesan or other hard cheeses. Many recipes include a cheese sauce known as béchamel or Besciamella, which is made from butter, flour, milk, and cheese.
- **Vegetables:** Options may include carrots, celery, and garlic, often sautéed to create a base for the meat sauce.

**Additional Ingredients:** 
Recipes vary and may include optional items such as:
- Ground pork or turkey as meat alternatives.
- Dry red wine or broth for added flavor in the meat sauce.
- Seasonings like thyme, oregano, Worcestershire sauce, and sugar to balance acidity.
- Nutmeg in cheese sauces for enhanced flavor.
- Fresh herbs for garnish.

**Dietary Alternatives:**
Lasagna can be adapted for various dietary preferences:
- **Vegetarian:** Substitute ground meats with vegetables or plant-based meat alternatives. 
- **Vegan:** Use dairy-free cheeses and replace eggs with alternatives like flaxseed meal or silken tofu in cheese mixtures.
- **Gluten-Free:** Use gluten-free lasagna noodles or vegetable slices (like zucchini) in place of pasta.

Lasagna is known for its versatility, allowing for numerous substitutions and variations based on personal preference or dietary restrictions. The dish can often be pre-prepared and frozen, making it convenient for meal planning.
