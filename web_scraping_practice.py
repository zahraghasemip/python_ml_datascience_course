from bs4 import BeautifulSoup 
import urllib.request
from IPython.display import HTML 
import re 
import ssl
context = ssl._create_unverified_context()

r = urllib.request.urlopen('https://www.wikipedia.org' , context=context).read()
soup = BeautifulSoup(r ,'html.parser')
type(soup)

print(soup.prettify()[:1000])

file = open('parsed_data.txt' , 'w')
for link in soup.find_all('a', attrs = {'href': re.compile('^http')}):
    soup_link = str(link)
    print(soup_link)
    file.write(soup_link)

file.flush()
file.close()
# print(soup.get_text())