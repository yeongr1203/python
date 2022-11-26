# 복습

# 메소드 => 데이터에 연결된. 즉, 결합된 function(함수).
#           데이터 안에 있음.

"nico" 
#  단순 string아닌 함수

print("nico".endswith("a"))
# 답은 false, nico는 a로 끝나지 않음.
#  이렇게 메소드를 사용하는 방식이 있다.

# 우리가 찾고 사용할 때, 
# 데이터 이름 뒤 . 점을 찍은 후 메소드를 작성하면 됨.
#  메소드 = 함수. 똑같이 소괄호를 쓰면 실행한다는 뜻.
# 동일하게 소괄호 안에 argument 넣을 수 있음.

# 만약 함수가 독립적 사용이 된다면 "함수"라고 부른다.
# 하지만 데이터에 결합된 함수는 "메소드"라고 부른다.


numbers = [ 5, 3, 1, 5, 7, 3, True, "True", 12]

numbers.append(["pizza", "burger"])
print(numbers)
numbers.clear() # List 값 전부 지움.
print(numbers)

#  만약 numbers를 가지고 True에 접근하고자 한다면,
print(numbers[6])
print(numbers[-1])



