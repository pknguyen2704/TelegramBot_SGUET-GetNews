import requests
from bs4 import BeautifulSoup

r = requests.get("https://uet.vnu.edu.vn/category/tin-tuc/tin-sinh-vien/")
soup = BeautifulSoup(r.text, 'html.parser')
mydivs = soup.find_all("div", {"class": "post"})
for new in mydivs:
    print()