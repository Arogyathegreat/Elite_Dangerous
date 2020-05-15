import requests
import re
from bs4 import BeautifulSoup

url = "http://edtools.ddns.net/expl.php?a=v&f=synuefe+vm-d+c15-10&t=diaguandri&r=50&ap=on"
response = requests.get(url)

soup = BeautifulSoup(response.text, 'lxml')

table = soup.find('table')

entry = []
for row in table.find_all('tr'):
    test = []
    for column in row:
        test.append(column.text)

    planets = test[3]
    # planets = re.sub(r"^([A-Z]{3})$", r" ", planets).strip()
    test[3] = planets
    print(re.findall(r"^([A-Z]{3}+)$", planets))

    entry.append(test)


