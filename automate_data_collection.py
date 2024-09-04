import requests 
response = requests.get('https://www.python.org')
print(response.headers['Content-Type'])

import difflib 
flines = 'python is a good language'
glines = 'python is useful'

d = difflib.Differ()
diff = d.compare(flines,glines)

for line in diff:
    print(line)

