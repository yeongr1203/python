#  Loop = 반복문.
websites = (
    "google.com",
    "airbnb.com",
    "https://twitter.con",
    "facebook.com",
    # "tiktok.com"
    "https://tiktok.com "
)

for website in websites:
    # for loop에서 현재 실행중인 item에 접근 가능.
    # print(websites)
    # if website.startswith("https://"):  
    # # if문 method 사용함.
    #     # https://로 시작.
    #     print("good to go")
    # else:
    #     print("we have to fix it")
    
    # https:// 실행하지 않을때!
    # 즉, 이 코드는 https://로 시작하지 않는 website에서만 작동함.
    if not website.startswith("https://"):
        # true || false 를 return하는 method 사용.
        # 웹사이트가 "https://"로 시작하는지 물어보고
        # https:// 로 시작하지 않으면 === True

        website = f"https://{website}"
        # True로 이 코드가 작동하면, "https://"로 시작하지 않는 website를 가져와서
        # website 변수는 이제 "https://"를 붙인 값으로 업데이트 해줘.

    print(website)
    # 출력하면 https://가 붙어서 출력됨.
    # print(website)는 모든 website에서 작동함.
    # if문 밖에 위치해 있기 때문에!
    
