'''
# <<아래의 내용을 토대로 프로그램을 작성해보세요.>>
# 1. 다음과 같은 메뉴와 가격을 key와 value로 사용하여
# 사전형 자료를 만들어보세요(변수명은 menu)
#  칼국수(6000원), 비빕밥(5500원), 돼지국밥(7000원),
#  돈까스(7000원), 깁밥(2000원), 라면(2500원) 

menu = {'칼국수':6000, '비빕밥':5500,'돼지국밥':7000,'돈까스':7000,'김밥':2000,'라면':2500}

# 2. 위에서 만든 사전형 자료 menu 변수에서 가격이 6000원 미만에
# 해당하는 메뉴와 가격을 출력하는 코드를 작성하세요. 

for me in menu:
    if menu[me] < 6000:
        print(f"{me}:{menu[me]}원")
    
# 3. 사용자 입력으로 메뉴와 가격을 입력 받아  menu 변수에 자료를
# 추가 할 수 있도록 하시오.(동일한 메뉴는 가격만 변경)

add_menu = input("메뉴를 입력하세요 : ")
add_price = int(input("메뉴가격을 입력해주세요 : "))
if add_menu in menu:
    menu[add_menu] = add_price
else:
    menu.update({add_menu:add_price})

# 4. 메뉴를 자동으로 선택하여 출력하게 만들어 보세요.   
sel = input("메뉴를 자동으로 출력하겠습니까?(Y/n) ")
if sel == 'Y' or sel != 'n':
    for me in menu:
        print(me,menu[me],'원')
    print()


### set클래스 
# 여러개의 자료를 비순서로 적재하는 가변길이 비순차 자료구조
# 
#  변수 = {값1,값2,값3,....}
#
#  특징 
#  - 중복 허용 X
#  - 순서가 없기 때문에 색인(index)사용할 수 없다
#  - 객체에서 제공하는 함수를 이용하여 추가, 삭제 및 집합 연산 등이 가능함. 
# 
#  1)중복불가 
se = {2,3,4,3,1}  # 숫자인 경우에는 정렬 표시됨.
print(len(se))
print(se)

st = set('hello')  # set() : 셋 타입을 생성하는 함수
print(len(st))
print(st)

#  2) 요소 반복
for d in se:
    print(d, end=' ')
print() 

for s in st:
    print(s, end=' ')
print() 

#  3) 집합 관련 함수
#  - union([set타입 자료]) : 합집합 
#  - difference([set타입 자료-빨집합]) : 차집합
#  - intersection([set타입 자료]) : 교집합
#  - add() : 집합에 원소을 추가하는 함수
#  - discard() : 집합에 있는 원소를 제거

se2 = {2,4,6,8}
print(se.union(se2))            # {1, 2, 3, 4, 6, 8}
print(se.difference(se2))       # {1, 3}
print(se.intersection(se2))     # {2, 4}
se.add(7)                       # 원소를 추가
print(se)


st2 = set('world') # => {'w','o','r','l','d'}
print(st.union(st2))
print(st.difference(st2))
print(st.intersection(st2))
st.add('test')
print(st)

## 값의 타입은 상관하지 않아요.
lst = ['test','user','server','data']
print(set(lst))
 
## set을 사용하는 예시 : 중복된 원소를 제거

# python의 문자열 
#  : 파이썬의 사용하는 문자열 처리
# 
# (특징)
#  1)인덱싱을 이용한 참조 가능
string = 'python string'
#         0123456789...(index값)
print(string[0])    # p
print(string[7])    # s
print(string[-1])   # g
#  2)슬라이싱을 이용한 참조
print(string[:6])   # python
print(string[0::2]) # pto tig
#  3)문자열 반복문(for)
st = 'python string for'
for x in st:
    print(x,end=" ")
print()


# 문자열 함수 
#  -find(str) : 문자열에서 특정 문자열을 찾아서 해당 문자의 index값을 반환
#  -count(str) : 문자열에서 특정 문자열을 찾아서 해당 문자열의 수를 반환 
#  -lower() : 문자열에서 영문 대문자를 소문자로 변경하여 반환
#  -upper() : 문자열에서 영문 소문자를 대문자로 변경하여 반환
#  -strip() : 문자열에서 양쪽 공백 또는 문자를 제거하여 반환
#  -lstrip() : 문자열에서 왼쪽 공백 또는 문자를 제거하여 반환
#  -rstrip() : 문자열에서 오른쪽 공백 또는 문자를 제거하여 반환
#  -replace(old,new) : 문자열에서 왼쪽(old)문자열을 찾아서, 오른쪽(new)문자열로 변경
#  -split() : 문자열을 특정 문자를 기준으로 분리 -> 반환값을 리스트

#print(help('str'))

# find 예제
st = 'python string'
#     0123456789...
print(st.find('string'))    # 7
# find(str,시작인덱스,끝인덱스)
print(st.find('t'))         # 2
print(st.find('t',3))       # 8
# find()가 문자열을 찾지 못한 경우의 반환값 : -1
print(st.find('t',9))       # -1

# count()
st = 'python string'
print(st.count('t'))        # 2
# count(str,시작인덱스,끝인덱스)
print(st.count('t',6))      # 1

# lower() 
st = 'PYTHON STRING'
print(st.lower())           # 반환값으로 변경된 내용을 전달. 원본X
print(st)
st1 = st.lower()
print(st1)

# upper()
st = 'python string'
print(st.upper())
st2 = st.upper()
print(st2)

# strip() : 양쪽에 인자로 전달 받은 문자열을 제거
#         인자값이 없는 경우, 공백을 제거.
st = '        python string        '
#print(st)
print(f"[{st}]") 
st1 = st.strip()
print(f"[{st1}]") 

# lstrip()
st2 = st.lstrip()
print(f"[{st2}]") 

# rstrip()
st3 = st.rstrip()
print(f"[{st3}]") 

# replace(old,new)
st = 'python string'
st1 = st.replace('string', '문자열')
print(st1)              # python 문자열

# split(str)** 문자열을 str에 있는 문자를 기준으로 분리 -> list로 저장
st = 'python string'
st1 = st.split()        # 공백을 기준으로 .... 
print(st1)              # ['python','string']

# split()을 이용한 입력문자 값 분리
values = input("입력 : ").split()   # 입력 => I am a student
print(values, type(values))

# 예제1. 결합 및 연산
A = 'Have a'
print(A)
B = ' Nice Day!'
C = A + B       # 'Have a' + ' Nice Day!'
print(C)        # Have a Nice Day!
print(C*3)      # 반복
A += ' Nice Day!!!' #확장
print(A)

# 예제2
str1 = 'Python is Easy. 괜찬죠? 아니야? 아님 말해요!!!'
print(str1)
print(str1.upper())
print(str1.lower())
# swapcase() : 영문 대소문자를 변경. 대문자 -> 소문자, 소문자 -> 대문자
print(str1.swapcase())
str2 = str1.lower()
# title() : 영문 단어의 시작을 대문자로 변경
print(str2)                 # python is easy. 괜찬죠? 아니야? 아님 말해요!!!
print(str2.title())         # Python Is Easy. 괜찬죠? 아니야? 아님 말해요!!!

# 문제1. 
# 1)아래의 문장 주어진 조건에 맞게 변경
# "NevEr-eVer 100gIVe Up" [변경전]
# "Never-Ever 100Give Up" [변경후]
st = "NevEr-eVer 100gIVe Up"
st1 = st.title()
print(st1)

# 2)Have a nice day 문자열에서 다음 알아오기 
# 'a', 'day', 'dak'의 갯수 알아오기
st2 = "Have a nice day"
print('a의 개수 : ',st2.count('a'))
print('day의 개수 : ',st2.count('day'))
print('dak의 개수 : ',st2.count('dak'))

# 문제2. "It is a fun python class" 문자열의 길이,
# 문자 'a'의 개수, 's'의 개수를 출력하는 코딩 (함수 쓰지마세요... )
st3 = "It is a fun python class"
cnt = cnt_a = cnt_s = 0
for i in st3:
    cnt += 1   # 문자열 길이
    if i == 'a':
        cnt_a += 1
    elif i == 's':
        cnt_s += 1
print("문자열의 길이 : ",cnt)
print("문자열의 'a'의 개수 : ",cnt_a)
print("문자열의 's'의 개수 : ",cnt_s)

# 문제3. "Have a nice day" 문자열을 가지고 다음을 처리하세요.
#  1)각각 find와 index를 사용하여 "day"문자의 위치를 찾으세요.
#  2)각각 find와 index를 사용하여 "kkk"문자의 위치를 찾으세요. 
#  3)find를 사용하여 첫번째, 두번째, 세번째, 네번째 'a'의 위치를 
#   출력하세요.

st4 = "Have a nice day"
print("find('day') : ",st4.find('day'))
print("index('day') : ",st4.index('day'))
print("find('kkk') : ",st4.find('kkk'))
# print("index('kkk') : ",st4.index('kkk'))

idx = st4.find('a')
print("find : 첫번째 a의 위치 : ",idx)
idx = st4.find('a',idx+1)
print("find : 두번째 a의 위치 : ",idx)
idx = st4.find('a',idx+1)
print("find : 세번째 a의 위치 : ",idx)
idx = st4.find('a',idx+1)
print("find : 네번째 a의 위치 : ",idx)

#[ Quiz ] : List 정의하여 첨자 위치 저장
# a의 총 개수와 첨자의 위치를 출력 하시오
# st = 'Have a nice day Have a nice day Have a nice day'
#  
#(결과) 
# a 개수 : 9
# 첨자 : [1, 5, 13, 17, 21, 29, 33, 37, 45]
str1 = 'Have a nice day Have a nice day Have a nice day'
lst = []
idx = 0
while True:
    idx = str1.find('a',idx)
    if idx != -1:
        lst.append(idx)
        idx += 1
    else:
        break
print("a 개수 : ",str1.count('a'))
print("첨자 : ",lst)

# strip() : 양쪽에 있는 공백 또는 문자를 제거
st = "   파이썬   "
print("[{}]".format(st))
print("[{}]".format(st.strip()))

st2 = "파이썬파"
print(st2)
print(st2.strip("파"))          # 이썬
print(st2.lstrip("파"))         # 이썬파
print(st2.rstrip("파"))         # 파이썬

st3 = "--1-파이썬-1--"
print(st3)                      # --1-파이썬-1--
print(st3.strip("-"))           # 1-파이썬-1
print(st3.lstrip("-"))          # 1-파이썬-1--
print(st3.rstrip("-"))          # --1-파이썬-1

# replace()함수 사용
st = "2015-06-05"
#     0123456789 (index)
print(st)
print(st.replace('2015','2022'))
print(st[0:4])
print(st.replace(st[0:4],'2022'))

# split(str) : 특정문자(str)를 기준으로 문자열을 나누는 함수 -> 리스트로 반환
st = "Never Ever Give Up"
a = st.split()
print(st)
print(a,type(a))

st2 = "하나:둘:셋"
st3 = "1,2,3"
b = st2.split(':')
c = st3.split(',')
print(b,type(b))
print(c,type(c))

st4 = "하나둘셋넷"
d = st4.split()
print(d,type(d))

# splitlines() : 개행('\n')를 기준으로 문자열을 나누는 함수 -> 리스트로 저장
st = "Naver\nEver\nGive\nUp"
print(st)
print(st.splitlines())      #['Naver','Ever','Give','Up']
'''
# 여러줄 문자열 처리 : ''' ~ ''', """ ~ """
st = """Naver Ever Give Up
Naver Ever Give Up
Naver Ever Give Up
Naver Ever Give Up
Naver Ever Give Up"""
print(st)
a = st.splitlines()
print(a)
"""
# join() : 지정한 문자열을 기준으로 문자열 데이터를 결합 -> str
st='123'
print(st.join('%%'))            # %123%
print('%'.join(st))             # 1%2%3

#아래의 리스트를 문자열로 변경해보세요. "I am a student" 로 변경.. join()을 이용
lst=['I', 'am', 'a', 'student']
print(' '.join(lst))

lst1 = ["","123","456"]
print("".join(lst1))                # 123456
print("-".join(lst1),type("-".join(lst1)))  # -123-456

# st = "2015-06-05"
lst = ['2015','06','05']
st = "-".join(lst)
print(st)                           # 2015-06-05

#Python 문자열 실습 문제
#문제1. input() 함수로 이름과 나이 값을 입력 받을 때 한번에 입력
#      받아 처리하고 출력하는 코드를 작성하시오. 
#  예)
#   이름과 나이를 입력하세요 : 홍기동 18
#   => 이름 : 홍길동 , 나이 : 18 살
text = input("이름과 나이를 입력하세요 : (예] 홍길동 18) : ")
name, age = text.split()
print(f"이름 : {name}, 나이 : {age}살")
#문제2. input() 함수로 입력 받은 수의 더하기,빼기,곱하기,나누기의 
#      간단한 수식을 처리할 수 있도록 코드를 작성하시오.
#      예) 계산식을 입력하세요 : 5+5 
#          계산 결과 : 10
#  

import os

while True:
    os.system('cls')
    calc = input("계산할 수식을 입력하세요[ex) 5+5] : ")
    if '+' in calc:
        # 더하기 연산
        num1, num2 = calc.split('+')
        num1 = int(num1);num2 = int(num2)
        print("계산 결과는 : ",num1 + num2)
    elif '-' in calc:
        # 더하기 연산
        num1, num2 = calc.split('-')
        num1 = int(num1);num2 = int(num2)
        print("계산 결과는 : ",num1 - num2)
    elif '*' in calc:
        # 더하기 연산
        num1, num2 = calc.split('*')
        num1 = int(num1);num2 = int(num2)
        print("계산 결과는 : ",num1 * num2)
    elif '/' in calc:
        # 더하기 연산
        num1, num2 = calc.split('/')
        num1 = int(num1);num2 = int(num2)
        print("계산 결과는 : {:.2f}".format(num1 / num2))
    else:
        print("수식입력이 잘못됐습니다.\n다시 입력해주세요!!!")
    sel = input("계속하겠습니까?(Y/n) : ")
    if sel == 'n':
        break
print("계산기 프로그램을 종료합니다.!!!")
"""
### 알고리즘 
#  알고리즘이란, 어떤 문제를 해결하기 위한 일련의 절다를 의미함. 프로그래밍이
# 논리적인 절차를 의미하는 로직을 기초로 삼ㅎ고 있기 때문에 이를 통해서 문제를 
# 해결하는 것을 말함. 
# 
# 
#  알고리즘의 만족 조건
#  -입력 : 외부에서 제공되는 자료가 있을 수 있다
#  -출력 : 적어도 한 가지 이상의 결과가 나올 수 있다 
#  -명백성 : 각 명령들은 애매한 부분이 없이 간단 명령해야 한다.
#  -유한성 : 반드시 종료 조건이 있어야 한다
#  -효과성 : 모든 명령들은 명백하고 실행 가능한 것이어야 한다 
# 

# 최대값/최소값(max/min)
# : 전체 자료의 원소들 중에 큰 값과 가장 작은 값을 선별하는 기본 알고리즘

# 1. 입력 자료 생성
import random
dataset = []
for i in range(10):
    r = random.randint(1, 100)
    dataset.append(r)
print(dataset)

# 2. 변수 초기화
vmax = vmin = dataset[0]

# 3. 최대/최소값 구하기
for i in dataset:
    if vmax < i :
        vmax = i
    if vmin > i :
        vmin = i

# 결과 출력
print("max = ", vmax, ' min = ',vmin)

## 정렬(sort)
dataset = [3, 5, 1, 2, 4]
for i in range(0,len(dataset)-1):
    for j in range(i+1,len(dataset)):
        if dataset[i] > dataset[j]: # swap조건
            tmp = dataset[i]
            dataset[i] = dataset[j]
            dataset[j] = tmp
    print(i,'번째',dataset)


## 검색(search)
# 검색 알고리즘은 순차검색과 이진검색(이분법)

dataset = [ 5, 10, 18, 22, 35, 55, 75, 103]
value = int(input("검색할 값 입력 : "))

low = 0 # 스타트 위치
high = len(dataset) - 1 # end의 위치
loc = 0
state =  False  # 상태변수

while (low <= high):
    mid = (low + high) // 2
    
    if dataset[mid] > value:  # 중앙값이 큰 경우 
        high = mid - 1 
    elif dataset[mid] < value: # 중앙 값이 작은 경우 
        low = mid + 1
    else: # 찾은 경우 
        loc = mid
        state = True
        break
if state:
    print(f"찾은 위치 : {loc}번째")
else:
    print("찾는 값이 없습니다.")

### 2장 4번과 3,4장의 연습문제 풀어서 다음주 월요일까지 메일로 
# kdw335552@nate.com

