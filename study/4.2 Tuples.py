# 리스트, 튜플 둘 다 정렬된 아이템의 집함!
# 둘 다 인덱스 0을 가지고 있다. 인덱스로 아이템에 접근 가능하지만 튜플은 불변, 리스트는 변할 수 있음.

# 튜플, 리스트 => 둘 다 나에게 정렬된 리스트, 즉 정렬된 아이템 집합을 준다. 

# 둘 다 아이템의 인덱스로 각각의 아이템에 접근할 수 있지만, Lisst로만 데이터를 변경할 수 있다.

# List => 이건 데이터를 수정해야하는 리스트인가?
# Tuple => 변경시키지 않는 데이터. 즉, 한 번 만들고 아무도 두 번 다시 건들게 하고 싶지 않을때. 

days = ("Mon", "Tue", "Wed")
"""
# 쓸수있는 메소드 => count, index
# 튜플은 불변하기 때문에 튜플을 만들면 내용 변경 불가.
# 튜플과 리스트의 차이.
# 튜플을 리스트로 변경하면 사용가능 => days = []
"""
print(days[0])
"""
튜플을 만들때는 소괄호()를 사용하지만, 그 안의 아이템에 접근 할 땐 대괄호[]를 사용해야한다.
튜플 역시 0부터 시작.
"""
print(days[-1])
# 0부터 시작하는 대신에 -1로 시작할 수 있다. => 튜플, 리스트 모두 적용함. 즉, 역순으로 출력 가능.

