import requests
from bs4 import BeautifulSoup


lookup_word = 'cold'
data = requests.get("http://www.synonym.com/antonyms/" + lookup_word)
soup = BeautifulSoup(data.text, "html.parser")

try:
    for item in soup.find_all("ul", {"class": "synonyms"}):
        words = item.find_all("a")
        for synonym in words:
            print(synonym.string)
except:
    print('Error!')
