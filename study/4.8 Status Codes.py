# Requests는 Python 코드에서 웹사이트로 request 보내는 걸 할 수 있게 해줌.

from requests import get

websites = (
    "google.com",
    "airbnb.com",
    "https://twitter.com",
    "facebook.com",
    "https://tiktok.com"
)

# website를 출력하는 대신 get(website)를 할 것이다.
# 그런데 get function은 response를 return해 줌.
# Response는 website의 응답.

# if문 실행시, 200일경우
result = {
    # 새로운 키를 dictionary안에 만듬.

}

for website in websites:
    if not website.startswith("https://"):
        website = f"https://{website}"
    # get(website)
    # 이 function이 무언가를 return 해주기 때문에 우린 그 값을 가져 올 것이다.
        response = get(website)
        # print(response)
        # Response [200] 이라고 출력시, 웹사이트가 성공적으로 응답했다는 뜻.

        # get function이 request한 response는 다른 것도 가지고 있는데, 예를 들어 상태코드.
        # print(response.status_code)
        # 코드를 얻었다는 건.
        if response.status_code == 200:
            # print(f"{website} is OK")
            result[website] ="OK"
        else:
            # print(f"{website} not OK")
            result[website] ="FAILED"
