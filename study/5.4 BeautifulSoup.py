from requests import get
from bs4 import BeautifulStoneSoup
# open(file,encoding='UTF-8')

base_url = "https://weworkremotely.com/remote-jobs/search?term="
search_item = "python"

response = get(f"{base_url}{search_item}")
if response.status_code != 200:
    print("Can't request website")
else:
    soup = BeautifulStoneSoup(response.text, "html.parser")
    # print(soup.find_all('title'))
    print(soup.find_all('section', class_="jobs"))

# if response.status_code != 200:
#     print("Can't request website")
# else:
#     print(response.text)
