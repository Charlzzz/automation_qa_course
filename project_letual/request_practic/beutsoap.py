import requests
from bs4 import BeautifulSoup

link = "https://deployhoroscope.ru/"

resp = requests.get(link).text
soup = BeautifulSoup(resp, "lxml")
# block = soup.find_all("div", id = "tool_padding")
# check_js = block.find("div", id = "javascript_check")

print(soup)






