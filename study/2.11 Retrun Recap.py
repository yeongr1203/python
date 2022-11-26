# return 개념

# 문자열안에 변수를 넣는 법
# my_name = "nico"
# my_age = 12
# my_color_eyes = "brown"

# print(f"Hello I'm {my_name}, I have {my_age} years in the earth, { my_color_eyes} is my eye color"
# )

# 주스메이커 만들기를 할 거야.
# 주스를 만드는 함수를 만들고 싶어.
# 주스에 얼음을 추가하는 함수를 만들고싶어.
# 주스에 설탕을 넣는 함수를 만들고 싶어.
def make_juice(fruit):
    return f"{fruit} + juice"
    # return은 함수를 끝내기때문에 바로 뒤에  print 사용해도 나오지 않음.!

def add_ice(juice):
    return f"{juice} + ice"

def add_sugar(iced_juice):
    return f"{iced_juice} + sugar"

juice = make_juice("apple")
print(juice)
colde_juice = add_ice(juice)
print(colde_juice)
perfect_juice = add_sugar(colde_juice)
print(perfect_juice)