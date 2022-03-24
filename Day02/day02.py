# 변수 선언
# 1. 변수이름 = 값
# 2. 변수이름1, 변수이름2,변수이름3 = 값1, 값2, 값3
# 3. 변수이름1 = 변수이름2 = 값1

from unittest import result


num1 ,num2, num3 =10, 20, 30
print(num1, num2, num3)

su1 = su2 = 100 #변수에 변수를 넣을때에는 메모리 저장장소가 같지만 그 값이 변한다면 저장 장소가 변한다.(su1만 장소가 바뀐다.)
print(su1,su2)
print(id(su1),id(su2))

su1 = 200
print(su1,su2)
print(id(su1),id(su2))

su1 = su1 + su2 
print(su1,su2)
print(id(su1),id(su2))

## input()함수 : 문자열을 입력받는 함수 반환값은 **str(문자열)**로 받는다! 
#print(type(input())) #문자열로 받아 처리한다.
#print(input("입력 : "))

#문자형 숫자 입력

# num = input("숫자 입력 : ")
# print(' num type : ', type(num))
# print(' num =',num)
# print(' num =', num*2) 

#숫자 연산을 위한 형변환

# num1 = int(input("정수 입력"))
# print('num1 =', num1*2) 


# num2 = float(input("실수 입력"))
# result = num1 + num2
# print('result =', result)
#정리, 인자(prompt)에 입력받기 위한 설명을 사용할수 있다.
# input()는 문자열로 입력을 받기 때문에, 숫자로 사용하기 위해서는 필요한 형태로 형변환을 반드시 해야한다.

#연습 ....input()을 사용하여 나이와 이름을 입력받아 다음과 같이 출력되게 해주세요.
# => '홍길동'님의 나이는 100세 입니다.

#내방식
# print("{}님의 나이는 {}입니다.".format(input("이름과 나이를 입력하세요\n"),int(input())))

# name = input("이름을 입력하세요")
# age = input("나이를 입력하세요")
# print("'{}'님의 나이는 {}세입니다".format(name,age))
# print(f"'{name}'님의 나이는 {age}세 입니다.")

##연산자
# 1. 산술 연산자 : 산술 연산을 위해 사용하는 연산자
#    종류 = "+" , "-", "*", "/", "//"(정수나누기), "%", "**"(제곱)

nu1 = 3
nu2 = 2
print(nu1 + nu2)  #더하기
print(nu1 - nu2)  #빼기
print(nu1 * nu2)  #곱하기
print(nu1 / nu2)  #나누기 결과는 float(실수)으로 반환됨 ==>1.5  
print(nu1 // nu2) #정수나누기는 3/2의 몫만 구한다. ==> 1
print(nu1 % nu2)  #나머지 ==>1
print(nu1 ** nu2) #제곱 ==>9

# 2. 비교(관계) 연산자 : 두항의 값을 비교(관계)하여 관계를 설명하는 연산자 ->Bool로 True or False를 반환, 값의 기준은 좌항
#    종류 = "==" : 두항이 값이 같다. "!=" : 두항의 값이 같지 않다. ">" : 값이 크다. "<" : 값이 작다. 
#          ">=" : 값이 크거나 같다. "<=" : 값이 작거나 같다. 
print(3==3) #True
print(3!=3) #False
print(3>2)  #True
print(3<2)  #False
print(3>=2)
print(3<=2)

# 3. 논리 연산자 : 두항의 값이 참인지 거짓인지 확인하여 판별하는 연산자-> Bool 로 반환
#    종류 = "and"(논리곱) : 두항의 값이 모두 True인경우 True를 반환, True = 1, False = 0 
#          "or"(논리합) : 두항중 하나라도 True인경우에 True 반환 
#          "not"(부정) : True이면 False를 False이면 True를 반환 
print("bool의 True의 int형변환 값은 :",int(True))
print(0 and 0) #False
print(1 and 0) #False     #and에서는 0이 있으면 무조건 False
print(0 and 1) #False
print(1 and 1) #True

print(0 or 0) #False
print(1 or 0) #True     
print(0 or 1) #True
print(1 or 1) #True

print(not 0) #True
print(not 1) #False

# 4. 멤버 연산자 : 왼쪽 피연산자의 값이 오른쪽 연산자 멤버 중 일치 여부를 확인하는 연산자.
#    종류 = in : 왼쪽 피연산자의 값이 오른쪽 피연산자에 존재하는 경우 True 
#          not in : 왼쪽 피연산자의 값이 오른쪽 피연산자에 존재하지 않는 경우 True
print(1 in (1,2,3))     #True
print(1 not in (1,2,3)) #False

# 5. 식별 연산자 : 식별값 비교 연산하여 처리하는 연산자
#    종류 = is :  두 피연산자의 식별값(객체타입)을 비교하여 동일 객체라면 True  
#          is not :  두 피연산자의 식별값을 비교하여 동일하지 않은 객체라면 True
num1, num2 = 1 , "1"
print(type(num1) is int)      #True
print(type(num2) is not int)  #True
print(type(num1) is not str)  #True
print(type(num2) is str)      #True

# 6. 비트 연산자 : 비트값을 연산 처리하는 연산자들...
#    종류 = & : 두 비트 and 연산처리하는 연산자 (논리곱)
#          | : 두 비트 or 연산처리하는 연산자 (논리합)
#          ^ : 두 비트에 대한 xor 연산처리하는 연산자 (배타적 논리 합)
#         << : 왼쪽 피 연산자의 비트를 왼쪽으로 오른쪽 숫자만큼 이동
#         >> : 왼쪽 피 연산자의 비트를 오른쪽으로 오른쪽 숫자만큼 이동 
# & : AND 비트 연산
#      00001010(10)
# &    00001101(13)   
#    ===============
#      00001000(8)
print(10&13)

# | : OR 비트 연산
#      00001010(10)
# |    00001101(13)   
#    ===============
#      00001111(15)
print(10|13)

# ^ : XOR 비트 연산 - 암호문 처리할 경우에 많이 사용됨, 두 비교 비트가 동일하면 0을 반환하고 둘중하나라도 1이라면 1
#      00001010(10) - 원본
# ^    00001101(13) - 키  
#    ===============
#      00000111(7)  - 암호
# ^    00001101(13) - 키 
#    ===============
#      00001010(10) - 원본
print(10^13)
print(7^13)

# << : 왼쪽 shift 연산자
#      00001010(10)
# <<             3   
#    ===============
#      01010000(80) 
#
# 특징 : 2의 제곱승으로 곱하는 정수 곱하기
print(10<<3)

# >> : 오른쪽 shift 연산자
#      00001010(10)
# >>             3   
#    ===============
#      00000001|(1)010
# 특징 : 2의 제곱승으로 나누는 정수 나누기
print(10>>3) 


'''
문제1. num1, num2, num3 = 5, 15, 27
   위 변수에 할당된 값을 사용하여 다음의 결과가 나오도록
   산술 연산자를 사용 하시오.
      ㄱ. -12  
      ㄴ. 75
      ㄷ. 25
      ㄹ. 5.4
      ㅁ. 3.0
 '''  
# num1, num2, num3 = 5, 15, 27
# print(num2-num3)
# print(num2*num1)
# print(num1*num1)
# print(num3/num1)
# print(num2/num1)   
# '''
# 문제2. 다음의 연산자를 보고 True와 False를 구분 하시오. 
#       ㄱ. 7 > 18        #False
#       ㄴ. 5 < 2         #False
#       ㄷ. 6 % 3 > 2     #False
#       ㄹ. 5 + 5 != 2 * 5#False
#       ㅁ. True == 1     #True
#       ㅂ. 1 == '1'      #False
#       ㅅ. 10 // 3 == 10 % 3 #False
#       ㅇ. 15 % 4 in (0, 1, 2) #False
# '''

# '''
# 문제3. input()으로 2개의 값을 받은 다음 더하기, 빼기, 곱하기, 나누기 연산을 
#     하여 그 결과를 출력하는 코드를 작성하시오.
# '''
# a = int(input('a값을 입력하세요'))
# b = int(input('b값을 입력하세요'))
# print(a,b)
# print (a + b)
# print (a - b)
# print (a * b)
# print (a / b)

# '''
# 문제4. 사용자로부터 이름, 키, 체중 값을 입력 받아 비만도를 구하고 출력하는 
#     코드를 작성하시오.
    
#     비만도 계산 식 : 비만도(%) = 현재 체중 / 표준 체중 * 100
#     표준 체중 계산 식 : 표준 체중 = (현재 키 – 100) * 0.9

#     출력 예제 : 홍길동님의 비만도는 112.15% 입니다. '''
# name = input("이름을 입력하세요.")
# height = float(input("키를 입력하세요"))
# weight = float(input("체중을 입력하세요"))

# classic = (height-100) * 0.9 
# bmi = (weight/classic) * 100
# print("{}님의 비만도는 {:.2f}%입니다.".format(name,bmi))

####제어문(if), 반복문(for,while)
# 제어문(if)
# 단순 if
#  사용형식 1
# if 조건식 :
#   실행문(종속문장1)
#   실행문(종속문장2)     ==> if 블럭
# 특징 : 조건문이 참일 경우에 종속문장을 실행
#     파이썬 에서는 다른 언어와 다르게 들여쓰기가 중요하고, 들여쓰기를 가지고 블럭을 구분함.
#[예제]
'''
num = int(input("정수입력")) 
if num % 2 == 0 :
    print("num 변수의 값은 짝수입니다.")
    print("num 변수의 값은 2의 배수입니다.")
print("if 다음 문장 실행")

#[예제2]
print("1. Easy Mode")
print("2. Hard Mode")
print("3. Exit")
num = int(input("번호를 선택하세요>>"))
if num ==1 :
    print("Easy Mode Start")
if num ==2 :
    print("Hard Mode Start")
if num ==3 :
    print("Game Exit")

#[예제3]
su = int(input("수 입력 :"))
if su == 1:
    print("1입력")
if su > 10:
    print("10보다 큰 값을 입력했습니다.")
if su < 10:
    print("10보다 작은 값을 입력했습니다.")

#[예제4]
x = 15
if x > 10 and x != 10: 
    print("x 변수의값은 10보다 크고 ,10과 같지 않다")
if x > 10 or x !=15:
    print("x의 값은 둘중 하나라도 참이면 참으로 결과를 반환")    
    
#[예제5]
su = int(input("1~10사이의 정수를 입력하세요. : "))
if su in(1,4,7):
    print("멤버에 있는 숫자입니다.") '''    
# if ~ else : if의 조건식이 참이면 , if의 종속문장을, 그렇지 않으면 else의 종속문장을 실행
# if 조건식 :
#   실행문(종속문장1)
#   실행문(종속문장2)    =>if 블럭
# else :
#   실행문(종속문장1)
#   실행문(종속문장2)    =>else 블럭 둘다 합쳐 하나의 if문으로 처리

'''[if문제] 
1. 입력한 데이터가 3의 배수인 경우를 출력하시오.
2. 절대값을 구하는 프로그램을 작성하시오.
3. 수를 입력 받아 짝, 홀수를 구분하여 출력하시오.
4. 두수를 입력받아 큰 수를 출력하시오.
5. 세수를 입력받아 큰 수를 출력하시오.
6. 두수를 입력받아 큰수가 짝수이면 출력하시오.
7. 두수를 입력받아 합이 짝수이고 3의 배수인 수를 출력하시오.
'''
'''
# 1.
num1 = int(input("숫자를 입력하세요"))
if num1 % 3 == 0:
    print(f"입력하신 수{num1}은 3의 배수입니다.")
else :
    print("입력하신 수는 3의 배수가 아닙니다..")
# 2.        
num2 = int(input("숫자를 입력하세요"))
if num2 < 0: 
    print(-num2)
if num2 > 0: 
    print(num2)
# 3.   
num3 = int(input("숫자를 입력하세요"))
num4 = int(input("숫자를 입력하세요"))  
if num3 % 2 == 0:
    print("짝수입니다.")
else :
    print("홀수 입니다.")    
# 4.
num5 = int(input("첫번째 숫자를 입력하세요"))
num6 = int(input("두번째 숫자를 입력하세요"))
if num5 > num6 :
     print(f"{num5}가 {num2}보다 크다")    
if num5 == num6:
     print("두수는 같습니다.")
if num5 < num6 :
    print(f"{num6}가 {num5}보다 크다") 
# 5.
num7 = int(input("첫번째 숫자를 입력하세요"))
num8 = int(input("두번째 숫자를 입력하세요"))
num9 = int(input("세번째 숫자를 입력하세요"))
if num7 > num8 and num7 > num9:
     print("더 큰 숫자{}입니다.".format(num7)) 
if num8 > num7 and  num8 > num9 :
    print("더 큰 숫자{}입니다.".format(num8))
if num9 > num7 and num9 > num8:
     print("더 큰 숫자{}입니다.".format(num9))
# 6. 
num10 = int(input("첫번째 숫자를 입력하세요"))
num11 = int(input("두번째 숫자를 입력하세요"))
if num10 > num11 and num10 % 2 == 0 :
    print("{}이 더 크고 짝수입니다.".format(num10))
if num10 < num11 and num11% 2 == 0 :
    print("{}이 더 크고 짝수입니다.".format(num11))
# 7.
num12 = int(input("첫번째 숫자를 입력하세요"))
num13 = int(input("두번째 숫자를 입력하세요")) 
num14 = num12 + num13
if num14 % 2 == 0 and num14 % 3 == 0 :
    print ("두수의 합 {}은 짝수이면서 3의 배수입니다.".format(num14)) 

# 중첩 if 구문 : if구문 안에 if구문을 사용하는 경우
# 다중 if 구문 : if ~ elif~ else 구문으로 if 와 elif 조건을 확인 부합되면 종속 실행
#              만약 조건에 부합되지 않은 경우에는 else를 실행 

# [예제7] 중첩 if 구문
num1 = int(input("첫번째 정수 입력: "))
num2 = int(input("첫번째 정수 입력: "))
sum = num1 + num2
if sum % 2 == 0:
    if sum % 3 == 0:
        print("입력하신 두수의 합은 {sum},3의 배수이면서 짝수 입니다.")
    else:
        print("입력하신 두수의 합은 짝수이지만 3의 배수는 아닙니다.")
else: 
     print("입력하신 두수의 합은 짝수가 아닙니다.")
     
# [예제8] 다중 if 구문(if ~ elif ~else)
num = int(input("1~4숫자를 입력 : "))
if num == 1 :
    print("1 입력")
elif num == 2 :
    print("2 입력")
elif num == 3 :
    print("3 입력")
elif num == 4 :
    print("4 입력")
else:
    print("잘못 입력했습니다.")
'''


'''
[Quiz1]
- 사용자로 부터 Gbyte 의 값을 입력받아 byte, kbyte,Mbyte로 각각 출력되게 만드시오.
- (1. byte, 2.kbyte, 3.Mbyte 선택)
- 단위 1024

[Quiz2]
- 인증프로그램을 만드시오.
- 아이디가 틀리면 등록되지 않은 아이디입니다 출력
- 비밀번호가 틀리면 비밀번호가 틀렸습니다 출력
- 아이디와 비밀번호가 일치한다면 인증 통과 출력
- old_id = test , old_pw = python123
'''
'''
# Quiz1
Gbyte = int(input("Gbyte값을 입력하시오."))
print("1. byte")
print("2. kbyte")
print("3. Mbyte")
num = int(input("번호를 선택하세요>>"))
byte = Gbyte*1024**3
kbyte = Gbyte*1024**2
Mbyte = Gbyte*1024 
if num == 1 :
    print(f"{Gbyte}의 byte단위는{byte}입니다.")
elif num == 2 :
    print(f"{Gbyte}의 kbyte단위는{kbyte}입니다.")
elif num == 3 :
    print(f"{Gbyte}의 Mbyte단위는{Mbyte}입니다.")
else :
    print("잘못 입력하셨습니다.")
# Quiz2    
old_id = 'test'
old_pw = 'python123'
print("인증프로그램 시작")
id = (input("아이디를 입력하시오."))
pw = (input("비밀번호를 입력하시오."))

if id == old_id :
    if pw == old_pw :
        print("인증 통과")
    else:
        print("비밀번호가 틀렸습니다.")
else:
    print("등록되지 않은 아이디 입니다.")
'''
# 삼항 조건문 : 조건식이 참인경우와 거짓인 경우 처리할 문장을 한줄로 작성
# 조건식 비교결과에 따라 선택적으로 실행문이 동작합니다.
# (형식)
#  변수 = 참 if (조건문) else 거짓
# [예제]
'''
num = 9 
result = 0
if num >=5:
    result = num * 2
else :
    result = num + 2
print("result = ",result)

print("삼항연산자")
result2 = num * 2 if num >= 5 else num + 2 # (True - 조건 - False)
print("result2 = ",result2)
'''
'''
# 문제4. 사용자로부터 이름, 키, 체중 값을 입력 받아 비만도를 구하고 출력하는 
#     코드를 작성하시오.
    
#     비만도 계산 식 : 비만도(%) = 현재 체중 / 표준 체중 * 100
#     표준 체중 계산 식 : 표준 체중 = (현재 키 – 100) * 0.9

#     비만도가 100 미만인 경우 "저체중"
#     비만도가 100~110 사이인 경우 "정상 체중"
      비만도가 110~120 사이인 경우 "과체중"
      비만도가 120~130 사이인 경우 "비만"
      그이상인 경우에는 고모비만으로 표현되게 작성하세요.
      출력예제 : 홍길동님의 비만도는 112.15%로 정상 체중입니다.
# 
# '''
name = input("이름을 입력하세요.")
height = float(input("키를 입력하세요"))
weight = float(input("체중을 입력하세요"))

classic = (height-100) * 0.9 
bmi = (weight/classic) * 100

if bmi < 100 :
    print("{}님의 비만도는 {:.2f}%로 저체중입니다.".format(name,bmi))
elif bmi >= 100 or bmi <= 110:
    print("{}님의 비만도는 {:.2f}%로 정상체중입니다.".format(name,bmi))
elif bmi >= 110 or bmi <= 120:
    print("{}님의 비만도는 {:.2f}%로 과체중입니다.".format(name,bmi))
elif bmi >= 120 or bmi <= 130:
    print("{}님의 비만도는 {:.2f}%로 비만입니다.".format(name,bmi))
else :
    print("{}님의 비만도는 {:.2f}%로 고도비만입니다.".format(name,bmi))