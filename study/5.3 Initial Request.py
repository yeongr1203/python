# 사이트 바로 웹스크랩핑할 수 없음.
# 스스로 코드를 검사(inspect)하고 지금까지 배운 모든 것을 사용해 이 웹사이트를 스크래핑 할 수 있도록 적응시켜야 함.
# 이유는 웹사이트가 변할 수 있기 때문에.
# 웹사이트는 계속 변하기 때문에 내가 맞춰야함.

# 스크래핑에 필요한 것은 url
# HTML 어떻게 되어있는지 보기. => 코드분석.

from requests import get

base_url = "https://weworkremotely.com/remote-jobs/search?term="
search_item = "python"

# get 해주기. 
response = get(f"{base_url}{search_item}")
# f 중요! 문자열 안에 변수를 넣을 수 있게 함.
# print(response)
#  결과 : <Response [200]> => OK
if response.status_code != 200:
    print("Can't request website")
else:
    print(response.text)



