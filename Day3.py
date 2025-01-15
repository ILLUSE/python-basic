# 1.Namespaces : 이름을 저장하는 공간
"""
이름 | 객체 메모리 주소
x      1004(주소)
"""
# x = 2023
# 1.2023이라는 int 객체 생성됨
# 2.x라는 변수 생성됨
# 3. x라는 변수에 2023이라는 int 객체의 주소값이 저장됨

x = 2023
y = x
print(hex(id(x)))
print(hex(id(y)))
print(x is y)
"""
이름 | 객체 메모리 주소
x      1004 
y      1004 (서로 같은 객체 가리킴)
"""
x = 2024
print(hex(id(x)))
print(hex(id(y)))
print(x is y)
"""
이름 | 객체 메모리 주소
x      1005 (x는 2024라는 새로운 객체를 가리킴)
y      1004
"""

x = [1, 2, 3]
y = [1, 2, 3]
print(x is y) # False
print(x == y) # True
"""
is : 객체의 주소값이 같은지 비교
== : 객체의 값이 같은지 비교
"""

# 2.Built-in Functions(내장함수)

# 3.변수 : 같은 값을 여러번 사용하기 위해 이름을 붙인 것
"""
rules
1.숫자 시작 x
2.소문자로만
3.파이썬 키워드 사용 x
4._로 시작 가능
5.최대한 자세한 단어 사용
"""

# 4.메모리 그리고 레퍼런싱
x = {'name':'John'} # {'name':'John'}이라는 객체 생성
y = x
y['name'] = 'Jane' # x와 y는 같은 객체를 가리키고 있기 때문에 x['name']도 'Jane'으로 바뀜
print(x['name']) # Jane

# 5.숫자형 제대로 알아보기
"""
int : 정수형
float : 실수형
boolean : 0/1
"""
print(5//2) # 2 (몫)
print(5//-2) # -3 (-3인 이유: 5 = -2 * -3 + 1)

bin(15) # 0b1111 (2진수)
oct(15) # 0o17 (8진수)
hex(15) # 0xf (16진수)

round(3.1415, 2) # 3.14 (소수점 둘째자리까지 반올림)

# import modules
import math
import random

math.sqrt(16) # 4.0 (x의 제곱근)
math.log(100,10) # 2.0 (y을 밑으로 하는 x의 로그값)

random.random() # 0.0 ~ 1.0 사이의 난수 생성
random.randint(1, 10) # x ~ y 사이의 난수 생성

print(1.1 + 2.2 == 3.3) # False (부동소수점 문제)
# 1.1을 저장하는 것이 아닌 1.1과 가장 가까운 부동소수점을 저장하기 때문에 오차가 발생


