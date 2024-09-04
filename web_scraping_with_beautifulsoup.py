from bs4 import BeautifulSoup 
filepath = '.\\data\\our_html_code.html'
with open(filepath, 'r', encoding='utf-8') as file:
    html_content = file.read()

soup = BeautifulSoup(html_content, 'html.parser')
print(soup.prettify()[0:300])

# tag names
soup = BeautifulSoup('<h1 attribute_1="heading 1"> test beautiful soup</h1>' , 'html.parser')
tag = soup.h1

tag.name = 'new_name'
tag['attribute_2'] = 'heading 1*'
del tag['attribute_1']
print(tag.name, tag.attrs)

