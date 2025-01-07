# GPTFoodSummarizer
This program is inspired by my personal use of ChatGPT. I would often use it in cooking - not for recipes, but to get inspiration and ask questions about dishes. Trying to get detailed information overall about a dish, such as the main ingredients and preparation, is difficult on any normal web search because it involves comparing multiple recipes, each of which will have individual quirks, to get the main idea. GPTFoodSummarizer will do this automatically, pulling multiple recipes from Google and providing an overall summary, while also incorporating information from the food's Wikipedia article if available.

## Usage:
An OpenAI API key is required to use this program.

```bash
$ export OPENAI_API_KEY=<openai key>
$ python main.py <foodname>
```

<foodname> must be wrapped in quotes if it is made of multiple words, e.g. "lentil soup"
