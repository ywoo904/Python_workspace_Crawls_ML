# 이전 수업 복습 문제
'''
문제1 윤년 구하기
윤년을 구하는 코드를 작성하시오
4의 배수는 윤년이 된다. 그외는 평년 4의 배수면서 100의 배수인 경우는 평년이다. 그외는 윤년
4 그리고 100의 배수이면서 400의 배수인 경우 윤년이다. 그외는 평년

year = int(input("년도를 입력하세요. : "))
if year % 4 == 0 :
    if year % 100 == 0 :
        if year % 400 == 0 :
            print(f"{year}년은 윤년입니다.")
        else : 
            print(f"{year}년은 평년입니다.")
    else :
        print(f"{year}년은 윤년입니다.")
else :
    print(f"{year}년은 평년입니다.")
'''
    
'''
문제 2 이름, 학번, 3과목의 성적을 입력받아 합계와 평균을 구하고
평균이 90이상이면 'A', 80이상이면 'B', 70이상이면 'C', 60이상이면 'D', 60미만은 F를 출력


name = input("이름 : ")
id = input("학번 : ")
kor = int(input("국어점수 : "))
eng = int(input("영어점수 : "))
math = int(input("수학점수 : "))
result = float((kor+eng+math)/3)
if result >= 90 :
    print("{} 학생의 평균점수는 {:.2f}, 성적은 A입니다.".format(name,result))
elif result >=80 :
    print("{} 학생의 평균점수는 {:.2f}, 성적은 B입니다.".format(name,result))
elif result >=80 :
    print("{} 학생의 평균점수는 {:.2f}, 성적은 C입니다.".format(name,result))
elif result >=80 :
    print("{} 학생의 평균점수는 {:.2f}, 성적은 D입니다.".format(name,result))
else :
    print("{} 학생의 평균점수는 {:.2f}, 성적은 F입니다.".format(name,result))
'''
   
'''
문제 3 
커피의 개당 가격은 2000원이다. 10개를 초과하면 초과하는 양에 대해서만 개당 1500원씩 받는다.
커피의 개수를 입력받아 금액을 출력하시오

coffee = int(input("커피의 개수 : "))
if coffee<=10:
    print("총 금액은 {}".format(coffee*2000))
elif coffee>10 :
    print("총 금액은 {}".format(20000+1500*(coffee-10)))
'''

'''
문제 4
정수를 입력받아 아래와 같이 출력하시오
3의 배수이면서 4의 배수 입니다.
3의 배수입니다.
4의 배수입니다.
0은 3의 배수도 4의 배수도 아닙니다.

num = int(input("정수를 입력하세요 : "))
if num == 0 :
    print("0은 3의배수도 4의배수도 아닙니다.")
elif num % 3 ==0 and num % 4 == 0 : 
    print("3의 배수이면서 4의 배수입니다.")
elif num % 3 == 0 : 
    print("3의 배수입니다.")
elif num % 4 == 0 :
    print("4의 배수입니다.")
else : 
    print(num,"은(는) 3의 배수도 4의 배수도 아닙니다.")
'''

## 다중 if문을 사용하여 여러 조건식을 볼경우에 범위가 작은 조건식을 먼저 정의

## for구문
# : 가장 대표적인 반복구문 중 하나로 주어진 조건에 따른 회차만큼 반복
# (형식)
# for 변수명 in range(반복횟수):
#       종속문장1
#       종속문장2
# (메인 프로그램 실행코드 진행)

# range(시작값, 끝값, 증강값) : 파이썬의 내장 함수

#for i in range(10):
#    print("A",i)

# 사용법(range())
#   1. range(종료값) - 시작값 0 , 증강값 +1 기본값으로 생략
#       :0부터 시작해서 종료값 이전까지의 값의 범위를 가짐.
#   ex) range(10) => [0,1,2,3,4,5,6,7,8,9]
#   2. range(시작값,종료값)
#       :시작값부터 종료값 이전까지의 값의 범위
#   ex) range(5,10) =>[5,6,7,8,9]
#   3. range(시작값,종료값,증강값)
#       :시작값부터 종료값 이전까지 값의 증/감값 간격의 값범위
#   ex) range(0,10,2) => [0,2,4,6,8]
#       range(10,0,-2) => [10,8,6,4,2 ]

# range(종료값) 예제2
for x in range(10): #[0,1,2,3,4,5,6,7,8,9] 초기값 : 0, 증가값 : 1, 조건식 : x < 10
    print(x,end=' ') # print()의 end인자값 설정하면 출력 후 마지막에 사용될 문자를 지정할 수 있음
                     # 사용 : end = '문자열' , 기본값은 end = '\n'
print()

# 예제2 for문(range(시작값,종료값))
for x in range(5,10): # [5,6,7,8,9] , 초기값:5, 증가값:1, 조건식: x<10 and x>=5
    print(x,end=' ')
print()

# 예제3 for문(range(시작값,종료값,증/감값)) - 증가값
for x in range(0,10,2): # [0,2,4,6,8] , 초기값:0, 증가값:+2, 조건식: x<10
    print(x,end=' ')
print()

# 예제4 for문(range(시작값,종료값,증/감값)) - 증가값
for x in range(10,0,-2): # [10,8,6,4,2] , 초기값:10, 증가값:-2, 조건식: x>0
    print(x,end=' ')
print()

# 예제5 for문
Sum = 0
for x in 'string': #['s','t','r','i','n','g']
    print(x,end='')
    Sum +=1
print();print(Sum)

# 예제6 for문 - list,tuple,dictionary...
i = 0
for x in [1,4,78,'test','A',1.80,100]:
    print(x,end= ' ')
    i +=1
print("\n",i,"번 반복함")

# 예제6 이중 for문 - for구문을 중첩해서 사용하는 것
Sum = 0
for x in range(10):         # 상위 for문 [0,1,2,3,4,5,6,7,8,9]
    for y in range(10):     # 하위 for문 [0,1,2,3,4,5,6,7,8,9]
        Sum +=1             # Sum = Sum + 1
print(Sum)

# 예제 7 이중 for문 예제
Sum = 0
for x in range(1,5,3):         # 상위 for문 [0,1,2,3,4,5,6,7,8,9]
    for y in range(5,0,-1):     # 하위 for문 [0,1,2,3,4,5,6,7,8,9]
        print("{} 상위 for문의 x의 값, {} 하위 for문의 y의 값".format(x,y))
        Sum = Sum + 1
print(Sum,"횟수만큼 반복함!")

print("=== 연습문제 ===")

'''
문제1 중첩 for문을 이용하여 구구단 표를 작성
(출력 예시)
2 x 1 = 2
2 X 2 = 4
...

for x in range(1):
    for y in range(1,10,1):
        print("2 X {} = {}".format(y,2*y))
print()
#for i in range(10):
#    print("A",i)
'''
'''
문제2 중첨 for문을 이용하여 구구단 표를 작성
2X1=2 2X2=4 2X3 =6 ...
3X1=3 ...
...

for x in range(2,10,1):
    for y in range(1,10,1):
        print("{}X{} = {}".format(x,y,x*y),end=' ')
    print()
print()

for x in range(1,10):
    for y in range(2,10):
        print("{}X{} = {}".format(y,x,x*y),end=' ')
    print()
print()
'''

'''
문제3 다음과 같이 출력되게 for구문을 작성하세요
상위for문이 0일때, 하위 for문 : 0 0 0 0 0
상위for문이 1일때, 하위 for문 : 0 1 2 3 4
상위for문이 0일때, 하위 for문 : 0 2 4 6 8
상위for문이 0일때, 하위 for문 : 0 3 6 9 12
상위for문이 0일때, 하위 for문 : 0 4 8 12 16
'''
for x in range(0,5):
    for y in range(0,5):
        print("{}".format(x*y),end=' ')
    print()
print()

'''
문제4 이중 for문을 사용하여 다음과 같이 출력되게 만들어 보세요
1 2 3 4 5
6 7 8 9 10
11 12 13 14 15
16 17 18 19 20
21 22 23 24 25
'''
for x in range(0,5):
    for y in range(1,6,1):
        print("{}".format(x*5+y),end='\t')
    print()
print()
'''
25 24 23 22 21
20 19 18 17 16
15 14 13 12 11
10 9 8 7 6 
5 4 3 2 1

'''
for x in range(5,0,-1):
    for y in range(0,5):
        print("{}".format(5*x-y),end='\t')
    print()
print()

'''
1 2 3 4 5
2 3 4 5 1
3 4 5 1 2
4 5 1 2 3
5 1 2 3 4
'''
for x in range(0,5):
    for y in range(0,5):
        print("{}".format((x+y)%5+1),end='\t')
    print()
print()

## while 구문
#   : 조건식이 참인 경우에 반족하는 반복문

# (형식)
# while (조건식):
#   종속문장1
#   종속문장2
# (메인 프로그램 코드 실행)

# 예)
# while x<10:
#   종속문장1
#   종속문장2
#   x = x + 1       # x += 1 => 조건식에 변화를 주는 값이 필요함
# (메인 프로그램 코드 실행)

# 예제 1 while구문을 이용한 반복문(짝수의 합, 홀수의 합)
i = 1
odd_sum = 0
even_sum = 0
while i <= 10:
    if i%2==0:
        even_sum +=i
    else :
        odd_sum +=i
    i += 1
print("짝수의 합 : {}, 홀수의 합 : {}".format(even_sum,odd_sum))

# while ~ else : while의 조건이 False가 되는 경우에 else가 실행됨
i = 0
while i < 5:
    print("{}번 종속문장 실행".format(i))
    i+=1
else : 
    print("조건식이 거짓인 경우에 실행문장")
print("메인 프로그램 실행 코드")

# while의 무한반복 
# : while 구문의 조건을 항상 참이되게 설정한 후에 반복문 내에 
# 제어를 위한 명령어를 실행하는 반복 구문
#  제어를 실행하는 명령어(반복문에 대한 제어) 
#  1. break => 반복의 종료
#  2. continue => 반복시 조건문으로 이동
# 
# (형식)
# while True:
#     종속문장1
#     종속문장2
#     (종료하기 위한 조건과 명령어 : break)
# 위와 같은 코드에서는 break를 사용하지 않으면 무한반복함.
# 무한히 반복되면서 다음으로 코드 진행되지 않기 때문에 정지한 것
# 같이 보이게 됨. 때문에 반복에서 벗어나기 위해서 
# "break"명령어를 적절히 사용해야 함.
# 
# (break 사용예)
# while True:
#     종속문장1
#     break
#     종속문장2
# (메인 프로그램 코드)
# 
# 프로그램 흐름 : 1) while의 조건식  2)종속문장1 3)break
#                4) 메인 프로그램 코드
# 
# (continue 사용예) => 반복문 종료는 아님. 조건식으로 이동
#
# while True:
#     종속문장1
#     continue
#     종속문장2
# (메인 프로그램 코드)
# 
# 프로그램 흐름 : 1)while의 조건식 2)종속문장1 3)continue
#               4)while의 조건식 5)종속문장1 6)continue 
#               7)while의 조건식 ... 
# 종속문장2는 실행하지 않음

'''
# 예제 2] break와 continue 사용 예제

# break 이용
while True:
    a = int(input("정수 입력[0입력시 종료] : "))
    if a == 0:
        break
    print("입력값 출력 : ",a)

# continue 이용
a = 0
while a < 5:
    a += 1
    if a == 3:
        continue
    print("a = {}".format(a))
'''
print("--- 연습문제 ---")
'''
# 문제1
쌀 100통이 저장되어 있는 창고에 암수 1쌍의 쥐가 있습니다.
쥐 한마리가 하루 20g씩 쌀을 먹고 있습니다.
10일마다 쥐의 수가 2배씩 증가하고 있다면
며칠만에 창고의 쌀이 모두 쥐의 먹이가 될까?
또, 이때에 쥐는 총 몇마리가 되어 있을까?
(쌀 한통은 1kg, 쥐는 쌀을 먹은 후 2배로 증가하는 조건)
결과 :  80일, 512마리
'''
rice = 100*1000
mou = 2
day = 1
while True:
    rice -= 20*mou
    if day % 10 == 0:
        mou *= 2
    if rice<=0:
        break
    day +=1
print("일수 : {}일 , 쥐의 마리수 : {}마리".format(day,mou))

'''
문제2 
1~100까지의 합을 구하는 코드를 작성
'''
Sum = 0
i = 1
while True:
    Sum +=i
    i+=1
    if i ==101 :
        break
print("1~100까지 합 : ",Sum)
'''
문제3
1부터 1식 증가하는 값에 대해 누적합을 구할 때 10,000보다 큰 누적합 값에 대해
마지막에 더해진 값이 얼마인지 구하시오
'''
Sum = 0
i = 1
while True:
    Sum +=i   
    if Sum>10000 :
        break
    i+=1
print("누적합 : {}, 마지막에 더해진 값 : {}".format(Sum,i))
'''
문제4
1부터 100사이의 소수를 출력하고 개수를 구하시오
'''
num = 2
prime_count = 0
print("1부터 100까지의 소수들 : ")
while num<=100:
    count = 0
    i = 1
    while i<=num:
        if num % i == 0:
            count += 1
        i+=1
    if count == 2:
        print("{}".format(num),end=' ')
        prime_count +=1
    num +=1
print("\n약수의 개수 : {}개".format(prime_count))

# bool형 자료를 이요한 알고리즘...(2진 알고리즘)
count = 0
for x in range(2,101):
    flag = True         # flag가 True면 소수
    ## 소수판별
    for y in range(2,x) :
        if x % y == 0 :
            flag = False
            break
    if flag:
        print(x,end='/')
        count +=1
print()
print(f"1~100사이에 소수의 개수는{count}개 입니다.")