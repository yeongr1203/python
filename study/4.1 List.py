# print("nico".endswith("o"))
# endswith을 호출하려면 문자열 생성이 먼저.
# 메소드와 함수의 차이점 ? 호출에 있음.
# 함수가 데이터와 결합이 되어 있다면 메소드라 부르고, 그렇지 않다면 함수라고 부른다.

days_of_week = ["Mon", "Tue", "Wed", "Thur", "Fri"]
print(days_of_week)

# print(days_of_week.count("Wed"))  #count는 내 리스트를 사용하여 단순히 count 해 줌.
# days_of_week.clear()    # clear는 직접적으로 데이터를 수정함(modify) = 내 리스트를 완전히 바꿈.
days_of_week.reverse()  # List가 reverse하고 데이터가 변경됨.(역순)
print(days_of_week)

days_of_week.append("Sat")  # append는 
print(days_of_week)

days_of_week.append("Sun")
print(days_of_week)

print(days_of_week[3])  # 컴퓨터는 0부터 시작!


"""
아래처럼 보다시피 숫자, 불리언, 문자열, 숫자로 이루어진 리스트를 모두 함쳐서 사용할 수 있다.
"""
days_of_week2 = [1,2,3,True, False, "hi", "black", [1,2,3]]
print(days_of_week2[2])