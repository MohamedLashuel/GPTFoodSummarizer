import argparse
import search
import chatgpt

# Allow one 'food' command-line argument
parser = argparse.ArgumentParser()
parser.add_argument("food")
args = parser.parse_args()

# Search for summary/recipes
foodpages = search.searchFoodPages(args.food)

# Summarize each individually
summ_pages = chatgpt.summarizePages(foodpages, args.food)

# Create a final summary from all and print it
print(chatgpt.finalSummary(summ_pages, args.food))