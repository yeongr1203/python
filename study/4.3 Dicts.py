# dictionary 데이터 구조

# dictionary => key value pair (키 값 쌍)
# 키 => 단어, 값 => 정의

# tuple = ( 소괄호 ) , List => [ 대괄호 ] , dictionary => { 중괄호 } 사용함. 
# player라는 딕셔너리 만들어, 그 안에 key, name, age,alive라는 속성을 만든 것.
player = { 
    # 'key': 'value' 순서로 작성.
    'name': 'nico',
    'age': 12,
    'alive': True,
    'fav_food': ["pizza","burger"]
 }
#  print(player. get('age'))
#  print(player. get('fav_food'))

#  dictionary 생성 후 삭제 및 추가. Tuple만 수정 불가.

# pop이란? key를 지운다는 것.
print(player)
player.pop('age')
print(player)
# player에 데이터 추가?
player['xp'] = 1500     #마지막에 추가됨.
print(player)

# List에 메소드 사용 가능함. 예) append
player['fav_food'].append("noodle")
print(player.get('fav_food'))
print(player['fav_food'])