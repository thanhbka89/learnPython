# find all links using regex
import requests
import re

url = input("Enter a URL: ")

website = requests.get(url)
content = website.text
try:
    links = re.findall('"((http|ftp)s?://.*?)"', content)

    for link in links:
        print(link[0])
except:
    print('Error!')
