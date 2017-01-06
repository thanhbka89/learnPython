import requests
#import bs4
from bs4 import BeautifulSoup

#print(bs4.__file__)
#print(dir(bs4))

url = 'http://manga24h.com/4160/Love-Riron.html'

response = requests.get(url)
parse_html = BeautifulSoup(response.text, 'html.parser')
#print(parse_html.prettify())
print(type(parse_html))
print("Lay 1 tag:")
print(parse_html.title)
print(type(parse_html.title))
print("Ten tag title:" + parse_html.title.name)
#print(dir(parse_html.title))
print(parse_html.title.text)

print('*****')
print(parse_html.p)

print("Ten tag cha cua tag base:" + parse_html.base.parent.name)
print("Lay gia tri thuoc tinh cua tag:" + parse_html.base['href'])
print(parse_html.base.get('href'))

print("Lay tat ca cac tag a:" )
#print(parse_html.find_all('a'))

#Lay tag theo ID
print(parse_html.find(id="link3"))

#extracting all the text from a page
print(parse_html.get_text())

def parsing_main_page(mainpageURL):
    chapterlist = []
    response = requests.get(mainpageURL)
    parsed_html = BeautifulSoup(response.text)
    #print parsed_html
    option_select = parsed_html.find("select", class_ = "form-control")

    if option_select is not None:
        parsed_chapters = option_select.find_all("option",limit=2000)
        for chapter in parsed_chapters:
            for attr,val in chapter.attrs.iteritems():
                if attr == 'value':
                    chapterlist.append(val)
    else:
        print("Cannot find manga list")
    return chapterlist

#ds = parsing_main_page(url)
#print(ds)