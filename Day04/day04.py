'''
6-1
*
**
***
****
*****
'''
for i in range(5):
    for j in range (i+1): 
        print('*',end="")
    print() #다 찍었으면 줄바꿈 
# or  
i=0 
while i<5 :
    x=0 #하위 반복문 초기값
    j= i+1 
    while x<j:   
        print("*",end="") 
        x +=1 
    print()
    i +=1 
print() 

''' 
6-2
*****
****
***
**
*
'''
for i in range(5): 
    for j in range(5-i): 
            print('*',end='')
    print() 
''' 
6-3
    *
   **
  ***
 ****
*****    
'''
for i in range(5): 
    for j in range(4-i): 
        print(' ', end="")
    for k in range (i+1): 
        print('*', end="")
    print() 
'''
6-4
*****
 ****
  *** 
   ** 
    *
''' 
for i in range(5): 
    for j in range (i): 
        print(' ', end="") 
    for k in range (5-i):
        print('*', end="")
    print()
'''
6-5 다이아몬드 
규칙:
1) 줄이 바뀔때마다 +2, 반이 넘으면, -2
2) 줄 수를 //2 (초기값), 줄수의 반 전 -1, 후 +1
    *
   ***
  *****
 *******
  *****
   *** 
    * 
'''
import os 
#os 모듈은 파이썬에서 제공하는 기본 라이브러리 모듈 
#os 와 관련된 함수들이 저장된 모듈 
#system() => os의 시스템 명령어를 사용할 수 있게 함 

import time 
#시간과 관련된 제공하는 기본 라이브러리 모듈 

i,j = 0,0; num= 1 
while num:  
    
    ln= int(input("홀 수 줄수를 입력해주세요: "))
    sp = ln//2; st = 1 ; flag = True 
    #한줄로 여러개 묶을 때 세미콜론 사용 
    #이진, boolean, flag기법. 어느 조건이 부합되면 반전시키기 
    #ln이 상위포문 
    for i in range(ln): 
        for j in range(sp):
            print(" ",end="") #공백찍기 
        for j in range(st): 
            print("*", end="") #별찍기  
        print() 
        if i == (ln//2): 
            flag= False 
        if flag: 
            sp -=1; st +=2 
        else: sp+=1; st -=2 
    num=int(input("계속 하겠습니까?(0.종료, 1.계속):"))

#랜덤함수: 임의의 값(난수)를 출력하는 하뭇 
#난수는 생성된 임의의 값을 의미한다. 
#랜덤 함수를 사용하기 위해서 모듈을 사용: random 
#모듈 사용방법: import[모듈명] 
# ex) import random #랜덤 모듈 전체를 로딩  
# or 
# ex) from [모듈] import [모듈내용] => 모듈 내 일부 정보를 로딩  
# import random[모듈] import random[함수]. #랜덤 모듈 내 random() 함수를 로드  
# 두 방식은 기능 사용방식에 차이가 존재함 
# import 모듈인 경우, [모듈명].[사용할 값] 
# from[모듈] import[모듈에 사용값]인 경우, [모듈에 사용한 값]을 그대로 사용  

from random import random 
print(random()) #random 모듈에 있는 random() 
                #0.0~1.0 미만의 임의의 값을 출력(float)
                
# 0.0 ~ 10.0미만의 임의의 값을 출력 (float)
from random import random 
print(random()*10)  

#0.0 ~ 10.0 미만의 값을 출력 (int) 
from random import random
print(int(random()*10))

#1~10 까지 출력 (int)
from random import random  
print(int(random()*10)+1) 

#예제1] 1~45까지 임의의 값 6개를 출력 
from random import random  #random 0.0~1.0  
for x in range(6): 
    print(int(random()*45)+1,end=" ")
print() 

#문제1] 1~100까지 랜덤값을 6개 출력하는 코드작성 
from random import random 
for i in range(6):
    print(int(random()*100)+1,end=" ")
print() 

#문제2] 1~100까지 랜덤값을 반복하여 출력하되 출력값이 50이 되는순간 반복이 종료되는 코드를 작성하세요 
from random import random 
while True: 
    rannum= int(random()*100)+1 
    print(rannum)
    if(rannum==50): 
        break
    
#문제3] 1~15까지 랜덤값을 중복없이 3개 생성하여 출력하는 코드를 작성 
from random import random 
num1,num2,num3= 0,0,0 

while True: 
    su=int(random()*15)+1
    if num1 != su:  
        num1=su
        break
while True: 
    su = int(random()*15)+1 
    if num1 != su and num2 !=su: 
        num2=su 
        break 
while True: 
    su= int(random()*15)+1  
    if num1 !=su and num2 !=su and num3 !=su: 
        num3=su 
        break 
print(f"{num1} {num2} {num3}")

#random 0.0~1.0 사이의 float 반환
#randint(a,b) int형태의 시작값 끝값 포함출력 
from random import randint 
print(randint(1,6)) 
print(randint(100,200)) 

#또 다른 random함수 
# -randrang ():범위 내 임의값 출력 

#예시)
# randrange(5,10) 5~10미만을 출력 
# randrange(5,10,2) 5,7,9 출력  

#예제3] 
from random import randrange
print(randrange(5)) 
print(randrange(5,10)) #스타트값 포함 
print(randrange(5,10,2)) #스타트값 포함 

# random 모듈 내에 choice(() 함수 
# 이 함수의 특징은 리스트와 같은 형태의 자료 중 일부를 랜덤하게 추출하는 함수  

# 예시)
# dice= [1,2,3,4,5,6] #리스트형  
# choice(dice) #리스트 

import random 
dice= [1,2,3,4,5,6] 
st= "Hello World" 
x= random(choice(st)) 
print("dice에서 추력된 값:", x)

from random import choice
dice= [1,2,3,4,5,6] 
st= "Hello World" 
x= choice(St)
print("dice에서 추력된 값:", x)

# 문제: 1~99까지 랜덤값 중에 짝수는 True,홀수면 False 
from random import choice 
from random import randint
rand=randint(1,99)
print("1~99중 랜덤 숫자는:",rand)
if rand %2==0:  
    print(f"True{rand}입니다.") 
else: 
    print(f"False{rand}입니다.")
    
'''
ASCII코드 
-미국 표준 문자코드로 7bit(0~127)로 하나의 문자를 표현할 수 있음  
-ASCI코드는 통신상 기본 문자코드로 사용됨  
1) 특징: 프린트 가능한 문자 95자, 나머지 33개 문자는 프린트가 불가능한 문자  
        프린트 가능한 문자의 시작 0x20(32) -> "공백"부터 시작  
2) 숫자는 0x30(48)="0"에서부터 0x39(57)="9"까지 값을 가진 10개의 코드 
3) 영문 대문자는 0x41(65)=> "A"에서 부터 0x5A(90)="Z"까지 
4) 영문 소문자는 0x61(97)=> "a"에서 0x7A(122) = "z" 까지 
5) ASCII 코드는 문자이나 숫자(정수)로 표현이 가능함  

# 숫자를 문자(ASCII)로 변경하는 함수: chr()
# ()안에 코드 값을 전달하면 그 값을 문자로 출력하는 함수 
'''
print(chr(65)) 
print(chr(0x41))

# 문제5] 'A'~'Z' 까지 임의문자 3자리를 출력하는 코드
from random import random, randint, randrange, choice
for i in range(3): 
    ch= int(random()*26)+65 #65~90까지 
    print(chr(ch),end=" ")
print() 
'''
리스트 자료형이란? 
    -데이터 목록을 다루는 자료형
    -리스트를 정의할 때는 "[]"을 사용 
    -리스트 안에는 어떤 종류의 자료형이든 상관없이 저장가능ㄷ
LIST 자료형의 기본사용(정의) 

(정의) 
변수명 =[ ] 
변수명 = [value1, value2, value3, value4,...]
(value들의 타입은 상관없이 가능) 

list() 를 이용한 리스트 생성 
변수명 = list() #비어있는 리스트를 선언
변수명 = list("Hello") #['H','e','l','l','o']
변수명 = list(range(5)) #[0,1,2,3,4]
'''
#예제1] 리스트 선언 및 값에 대한  처리 
lst=[1,2,3,4,5,6,7,8]
print(type(lst)) 
print(lst[0] ) #1
print(lst[3]) #4
#생성된 리스트에 대한 특정값 참조: index값 활용 
#indexing방법: 변수명[인덱스 값], 인덱스 값은  부터 시작 
# indexing을 이용한 list값 변경 
lst[0] = lst[5] 
print(lst[0]) 
print(lst) 

#리스트 자료의 길이 (요소[맴버]의 갯수): len() 
print("lst의 길이: ", len(lst))

#리스트의 결합1  
lst2= [9,10] 
print(lst+lst2)  #[6,2,3,4,5,6,7,8] + [9,10]
lst3= lst+lst2
print(lst3)

#리스트의 결합2(확장)
lst = lst+ lst2 
print(lst) #[6,2,3,4,5,6,7,8,9,10] 

#리스트의 반복 
print(lst2*3) #[9,10,9,10,9,10]

#max(): 최대값 , min(): 최솟값
# lst= [6,2,3,4,5,6,7,8,9,10]   
print(max(lst)) # 10
print(min(lst)) # 2 
print(sum(lst)) # 60
print(pow(4,2))

#변수를 선언, 3개의 정수를 입력받아 합의 출력을 코딩 
#출력결과 >> "합계"= "xx" 합계문자도 변수로 저장  
a= int(input("첫번째 변수를 선언하세요 "))
b= int(input("두번째 변수를 선언하세요 "))
c= int(input("세번째 변수를 선언하세요 "))
d= "합계"
Sum= a+b+c 
print(f"{d}={Sum}")

# 예제2] 리스트의 멤버를 변수처럼 상용 
lst= [0,0,0,"합계"]
lst[0]= int(input("첫번째 변수를 선언하세요 "))
lst[1]= int(input("두번째 변수를 선언하세요 "))
lst[2]= int(input("세번째 변수를 선언하세요 "))
Sum2= lst[0]+lst[1]+lst[2] 
print(f"{lst[3]}={Sum2}")


#List 인덱싱: 인덱스 값을 이용한 참조  
#1st= [1,2,3,4,5,6,7,8] 
#양의 index: 0 1 2 3 4 5 6 7 8 
#음의 index: -8 -7 -6 -5 -4 -3 -2 -1 

#예제3] List 인덱싱  
lst= [1,2,3,4,5,6,7,8]
#(+) 0 1 2 3 4 5 6 7 
#(-) -8 -7 -6 -5 -4 -3 -2 -1 
print("lst[]: ",lst)
print("lst[-1]:", lst[-1]) 
print("lst[-2]:", lst[-2]) 
print("lst[-3]:", lst[-3]) 

''' 
slicing방식을 이용한 시퀀스 객체(자료)접근 
slicing이란? 리스트와 같은 시퀀스 자료 값들의 범위로 접근하기 위해서 
사용하는 방법으로 시퀀스 자료의 일부를 잘라서 새롭게 생성한는 것을 의미  
(형식) 
    변수명[시작인덱스:끝인덱스]
    변수명[시작인덱스:끝인덱스:증감값]

예] 1st = [1, 2, 3, 4, 5, 6] 
    index  0  1  2  3  4  5 
    (-)   -6  -5 -4 -3 -2 -1 
lst[0:3] => [1,2,3] 
lst[0:3:2]=> [1,3]
lst[-6:-3] => [1,2,3,4] 
lst[-1:-3:-1] => [6,5,4]
1st[5:0:-3] => [6,3]
'''

##인덱스 생략 
print(lst[:3]) #시작값 생략: [1,2,3]
print(lst[3:]) #끝값 생략: [4,5,6]
print(lst[:])  #둘다 생략: [1,2,3,4,5,6]

#슬라이싱 후 새로운 리스트 생성 
list = [1, 2, 3, 4, 5, 6] 
slc1= list[3:6] #[4,5,6] 
print(slc1) 
slc2= list[1:5:3] #[2,5] 
print(slc2)
slc3= list[5::-1] #[6,5,4,3,2,1]
print(slc3)
slc4= list[-3:-1] #[4,5]
print(slc4) 

'''
리스트 함수들..
-append(value): 리스트 끝에 값 추가 
-extend(iter): 리스트 끝에 list, tuple, dic의 값을 하나씩 추가 
-insert(idx,value): idx(인덱스)에 있는 인덱스 위치에 특정값을 추가하는 함수  
========위 3개는 리스트에 값을 추가하는 메서드 
-pop([idx]): 인덱스를 지정하지 않으면 해당 인덱스 값을 반환 후 삭제  
            인덱스 값을 지정하면, 해당 인덱스 값을 반환 후 삭제 
-remove(value): 특정값을 찾아서 삭제하는 함수  
-clear(): 리스트의 모든 멤버를 삭제하고, 빈 리스트로 만드는 함수 
========위 3개는 리스트를 제거하는 메서드 
-count(value): 리스트 내에 특정값의 개수를 반환하는 함수 
-index(value): 리스트 내에 특정 값의 인덱스 값을 반환하는 함수 
-reverse(): 리스트의 멤버 순서를 뒤집어서 나열하는 함수  
-sort([reverse=False]): 리스트의 값을 오름차순(False), 내림차순(True) 정렬해주는 함수
''' 

lst2=[1,2,3,4,5,6,7,8] 
lst2.append('a') 
print(lst2) #=> len(lst2)->9 
lst2.append([9,10]) 
print(lst2) #=> len(lst2)-> 10 
print(lst2[-1]) #[9,10]

#extend(): 리스트 뒤에 추가 
lst1= [1,2,3,4,5,6,7,8] 
lst1.extend('abcdef')  
print(lst1) #문자도 리터럴 값이기 때문에 1씩 잘라서 삽입 

#insert(idx,value) : idx인덱스 위치에 값을 추가 
lst1=[1,2,3,4,5,6,7,8] 
# idx 0 1 2 3 4 5 6 7 
lst1.insert(3,'a') 
print(lst1) #[1, 2, 3, 'a', 4, 5, 6, 7, 8] a추가하고 나머지 한칸 밀린다 

#pop(): 맨뒤에 있는 멤버 반환 후 삭제, idx 넣으면 해당 인덱스 반환 후 삭제 
lst1=[1,2,3,4,5] 
a= lst1.pop() #a=5,lst1=>[1,2,3,4]
print(a) 
print(lst1) 
b= lst1.pop(2) #b=3, lst1=> [1,2,4]
print(b)
print(lst1)

#remove(value): value에 있는 내용을 검색 후 삭제  
#검색 시에 없으면 Error 반환 
lst1= [1,2,3,2,5,6,2,8] 
lst1.remove(2) #첫번째 2가 삭제  
print(lst1)    
lst1.remove(2) #두번째 2가 삭제  
print(lst1) 
lst1.remove(2) #세번째 2가 삭제  
print(lst1)
lst1.remove(2) #ValueError: list.remove(x):x not in list    
print(lst1) 

#clear() 
lst1= [1,2,3,4,5] 
lst1.clear() 
print(lst1)