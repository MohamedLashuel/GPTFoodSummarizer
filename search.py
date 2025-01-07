import requests
import re
import wikipedia
from bs4 import BeautifulSoup
from globals import *

# Extract body text from a requests response
def textFromPage(page):
    soup = BeautifulSoup(page.text, 'html.parser')
    return " ".join(soup.text.split())

# Recursive function to take responses until we have n successful ones
def getUpToNGoodResponses(links, n, sofar = []):
    if n == 0 or links == []:
        return sofar
    
    # Get the response for the first link, keep if it's successful
    r = requests.get(links[0])

    # Status code 200 = successful response
    if r.status_code == 200:
        return getUpToNGoodResponses(links[1:], n-1, sofar + [r])
    else:
        return getUpToNGoodResponses(links[1:], n, sofar)

# Perform a google search and get the text from the pages we find
def searchPages(search, n = 5):
    r = requests.get(f"https://google.com/search?q={search.replace(' ', '+')}")
    # Extract links corresponding to pages
    links = re.findall(r"""(?<=egMi0 kCrYT"><a href="/url\?q=)https://[^"' ]*(?=&amp;sa)""", r.text)
    pages = getUpToNGoodResponses(links, n)
    return [textFromPage(p) for p in pages]

# If wikipedia does not have the page we are asking for, 
# wikipedia.summary will error, so catch this case and return None
def tryWikipediaSummary(item):
    try:
        return wikipedia.summary(item)
    except wikipedia.exceptions.PageError:
        return None

# Get wikipedia summary and recipes and put them together
def searchFoodPages(food):
    recipes = searchPages(f"{food} recipe")
    wikisum = tryWikipediaSummary(food)
    return FoodPages(recipes, wikisum)