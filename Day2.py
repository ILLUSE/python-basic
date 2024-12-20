# list = [] 안에 객체들을 순서대로 모아놓은 객체
# 메모리 주소를 저장해놓은 것! (주소를 통해 데이터를 찾아감)
X = [0,[1,2],[3,4,5],['안녕',['하','세요']]]

print(X[0]) # 0
print(X[1][1]) # 2
print(X[3][1][0]) # 하 3번째 인덱스의 1번째 인덱스의 0번째 인덱스
print(len(X)) # 4

# dictionary = {} 안에 key와 value를 랜덤한 순서대로 모아놓은 객체
# key는 unique해야 함 / string, number, tuple만 가능
Y = {

'age': 30,
'age': 40, # 중복되면 뒤에 있는 값으로 덮어씌워짐
'hobby': ['soccer', 'baseball'],
'name':{
    'first': 'Jin',
    'last': 'Kim'
}

}
print(Y['age']) # 40
print(Y['hobby'][0]) # soccer
print(Y['name']) # {'first': 'Jin', 'last': 'Kim'}
print(Y['name']['first']) # Jin
print(len(Y)) # 3 (key의 개수)

# tuple = () 안에 객체들을 순서대로 모아놓은 객체
# list와 비슷하지만 수정이 불가능함
Z = (1,2,3,4,5)

# set = {} 안에 객체들을 랜덤한 순서대로 모아놓은 객체
# 각 객체들은 unique해야 함
# 수정 불가능한 객체만 들어갈 수 있음
A = {1,2,3,4,5}

# NoneType = null과 비슷한 개념
# 초기화 등을 할 떄 사용
value = None
if value is None:
    print("값이 아직 설정되지 않았습니다.")

#Mutuable vs Immutable
# Mutable = list, dictionary, set
# Immutable = tuple, string, number(int, float, complex)

#Quiz
# 100, 야구 출력하려면?
X = [
    {(1, 2, 3): ['그래프', '최고', [100, 200]],
     '취미': ['야구', '쉬기', '놀기']}
]

print(X[0][(1, 2, 3)][2][0])
# [0] : 리스트 안의 0번째 인덱스 ,[1,2,3] : 딕셔너리 안의 key, [2] : 리스트 안의 2번째 인덱스, [0] : 리스트 안의 0번째 인덱스

print(X[0]['취미'][0])
# [0] : 리스트 안의 0번째 인덱스, ['취미'] : 딕셔너리 안의 key, [0] : 리스트 안의 0번째 인덱스