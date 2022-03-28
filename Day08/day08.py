##변수의 범위
# 특정지역에서만 사용되는 지역변수(블럭내 사용)와 
# 지역에 상관없이 전 영역에서 사용되는 전역변수로 분류.(변수의 스코프-범위)
# 특정영역(블럭)은 함수 또는 블럭(if,for,while 등)등을 의미함 
# 전역변수-global, 지역변수-local 

#[에제1] 전역변수의 영역: 블럭에서만 동작 
#전역변수_global
var2 =2  #전역변수 

#함수정의  
def func(arg):
    var1 =1   # 지역변수 
    print(var1,var2,arg) 

#메인 
func(var2)
#지역변수_var1 =>  print(var1) 
#함수 블럭내 선언된 변수 에러발생:NameError: name 'var1' is not defined. Did you mean: 'var2'? 

#[예제2]
#전역변수_global
var2 =2  #전역변수 

#함수정의  
def func(arg):
    global var2 #전역변수 var2 호출  
    var2=10     #전역변수 var2=10
    print(var2,arg+2) 

#메인  
func(var2)
print(var2)

#함수 또는 블럭에서 변수명으로 데이터에 접근시 우선순위: 가까운 Local -> global
#[예제3]
#전역변수_global
var2 =2  #전역변수 

#함수정의  
def func(arg):
    global var2 
    var2=10    
    var1= 1 #콜러에 선언된 변수가 콜리의 변수와 겹쳐서 사용할 수 있다.  
    print(var2,arg+2) 
    def func(var2): 
        var2=1 #로컬변수 먼저실행 
        print(var2,arg,var1)
    func(var2)
#메인  
func(var2)
print(var2)

## 중첩함수 
# 중첩함수란 함수 내부에 또 다른 함수가 내장된 형태. 
# 외부함수: 내부 함수를 포함한 함수

# (형식) 
# def 외부함수(인수) : 
#       함수정의문1
#       def 내부함수(인수): 
#           함수정의문(내부)1
#           return 값 
#       return 내부함수 

# 파이썬의 중첩함수는 외부함수나 내부함수를 변수에 저장할 수 있다. 
# 이런 특성을 가진 함수를 일급함수(First Class Function)이라고 한다. 
# 특히 내부함수는 외부함수의 return 명령문을 이용하여 반환하는 형태의 함수를
# 클러저(Function Clour)라고 한다. 특징은 외부함수가 종료되어도 내부함수에서 
# 선언된 변수가 메모리에서 소멸되지 않는 상태로 내부함수를 사용할 수 있다.  

def a(): # 외부
    var1= 1
    print("a함수")
    def b(): #내부 
        print("b함수")
        print(var1)
    return b
b= a() #외부함수호출: a함수 
b()  #내부함수호출: b함수 

### 
data= list(range(1,101)) #1부터 100까지 숫자열 
# outer  
def outer_func(data):
    dataSet= data #data로 받은 값을 dataSet에 넣음 
    
    # inner 
    def tot():
        tot_val=sum(dataSet)
        return tot_val
    # inner 
    def avg(tot_val): 
        avg_val = tot_val / len(dataSet) 
        return avg_val
    
    return tot,avg #inner값 반환 => "함수클러저" / dataSet이 내부함수에도 변수적용될 수 있는 이유  

# 메인
# 외부함수 호출: data생성 
tot,avg= outer_func(data) # tot, avg= tot,avg(outer_func() return 값)

# 내부함수 호출 
tot_val= tot() #outer_func내에 있는 tot()함수 
print("tot=",tot_val)  
avg_val= avg(tot_val)  
print("avg= ",avg_val) 

#역할: 
#외부함수: 함수에서 사용할 자료를 만들고 내부함수를 포함하는 역할 
#내부함수: 외부함수에서 만든 자료를 연산하고 조작하는 역할 

#[QUIZ] 
'''
디폴트 매개변수를 이용한 요금 구하는 프로그램 만들기 
기본요금은 500원 환승이 없거나 환승 1회까지는 기본요금 
1회를 초과하는 환승의 경우 환승1회마다 요금의 2배씩 증가된다. 
Ex) 환승 2회인 경우: 1000원, 환승 3회일 경우:2000원] 
[장거리는 10000원으로 처리한다] 
1. 환승 안함 
2. 환승함  #(몇번 환승하는지 질의 후 요금계산)
3. 장거리 
<함수화 하여 작업, 함수처리 시 목적지에 대한 내용도 입력받아서 처리 
''' 
# 함수정의:transfer 
def transfer(dest,su=1,won=500): 
    for i in range(1,su):
        won *=2  
        if won >=10000:
            won= 10000
    return "{}까지 요금: {:,}원 입니다.".format(dest,won)  

def display(): 
    des=""; su=0 #목적지와 환승회수에 대한 초기값 
    num= input("1.환승안함\n2.환승함\n3.장거리\n번호선택>>") 
    dest= input("목적지 입력:  ")
    if num=='1': 
        result= transfer(dest)
    elif num == '2': 
        su= int(input("환승횟수를 입력")) 
        result= transfer(dest,su)
    elif num == '3': 
        result= transfer(dest,1,10000)
    else: 
        print("메뉴선택이 잘못됬습니다.") 
        return 
    
    print(result)
    
display() 

#match~case구문: 파이썬 3.10.0 이후에 도입...
# 다른 언어의 switch~case구분과 같은 동작 
#[예제1] 
def num_chk(st): 
    match st:
        case 1: 
            return "일" 
        case 2: 
            return "이"
        case 3: 
            return "삼" 
        case _: # Default 
            return "선택범위초과" 

st1= int(input("1~3까지 숫자를 입력하세요: "))
print("입력값은:"+num_chk(st1)+'입니다')

#예제 2 
def alpha_chk2(chk): 
    match chk: 
        case 'a'|'A': 
            return 'A'
        case 'b'|'B': 
            return 'B '
        case 'c'|'C': 
            return 'C '
        case 'd'|'D': 
            return 'A-C외 알파벳'

st2= input("알파벳 a-c중 하나 입력:")
print("입력한 알페벳은:", alpha_chk2(st2)) 

#연습: 국가명을 입력받아 해당 국가의 폰 번호를 출력하는 함수구현 
#01- United States 33-France  34-Spain 81-Japan 82-South Korea 
#코드가 없는 경우에는 "-1"을 반환값으로 하는 getPhoneCode()를 구현 
# (예) getPhoneCode("SouthKorea") -> 82

def getPhoneCode(country:str): 
    match country.lower(): 
        case 'unitedstates': 
            return 1
        case 'france': 
            return 33 
        case 'spain': 
            return 334
        case 'japan':
            return 81 
        case "southkorea": 
            return 82
        case _: 
            return -1

name = input("국가명을 입력하세요.")
print(getPhoneCode(name)) 

#lambda 함수: 
# 익명 함수로 일시적으로 사용하는 함수를 의미함. 
# 사용은 함수가 생성된 곳에서 필요한 경우, 사용한 후 버리는 함수  

# (형식) 
# lambda 인자리스트: 표현식

# 예) lam = lambda x: x**2 
#    print(lam(8))=> 출력결과: 64 

# lam2= lambda x,y: x+y 
# print(lam2(2,5))=> 출력결과: 7 
# 람다는 어디서든지 사용할 수 있는 임시함수의 역할 

lam = lambda x: x**2
print(lam(8)) 

lam2= lambda x,y: x+y
print(lam2(2,5))

# [예제1:] 람다와 함수의 결합. 
# 함수 
def swap(a,b):  
    return b,a
a= 100
b= 200

# 람다사용 
swap= lambda x, y:[y,x]
a= swap(10,20)
print(a,type(a))  

#[예제2]  
lam = lambda a: a*10 
lam2= lambda a,b: a+b 
noData = lambda : print("인자가 없는 lambda") 

#결과확인  
print(lam(10)) 
print(lam2(10,20))
noData() #람다처리가 인자값이 없는 함수의 형태로 만들어 주었음(함수화)  

#[예제3] 
def str_len(s): 
    return len(s)

string= ['bob','charles','alexander3','teddy'] 
#알파벳 순서로 정렬 => string.sort(key="str_len") =>문자열의 길이를 기준  
#string.sort(key=str_len) #function넣음 
string.sort(key=lambda s: len(s))  # 람다로 넣음  
print(string)

## lambda가 유용하게 사용되는 3가지 대표적 함수 
# filter: 특정 조건을 만족하는 요소만 남기고 필터링  
# map: 각 원소를 주어진 수식에 따라 변경하여 새로운 리스트를 반환 
# reduce: 차례대로 앞 2개의 원소를 가지고 연산, 연산결과가 또 다음 연산의 입력으로 진행됨. 
# 따라서 마지막까지 진행되며 최종 출력은 1개의 값만 남기게 된다. 

# filter(함수,리스트) 
# filter(function, iterable) -> 특정 조건의 요소만 남기고 필터링 
#                  리스트에 있는 내용을 함수에 대입하여 결과값을 처리 (True or False)
# 함수- 짝수만 반환하는 함수 
def even(n): 
    return n%2==0  

print(even(3)) # False반환 

nums= list(range(1,11)) 
filter_list= list(filter(even,nums)) 
print(filter_list)  

#lambda를 사용 
filter2_list= list(filter(lambda n: n%2==0,nums)) 
print("람다사용:",filter2_list)

#map: 특정 조건에 맞는 새로운 리스트를 생성
# 주어진 리스트, 리스트의 제곱을 한 숫자 새로운 리스트 

#map(func, iter1): 각 멤버를 func으로 동작시킨 후에 새롭게 리스트 생성  
nums= [1,2,3,4,5,6,7,8,9] 
print(list(map(lambda n:n**2, nums)))

# reduce 함수: functools 모듈 내에 존재함 
import functools 
a = [1,2,3,5,8] 
#리스트 안에 모든 숫자의 함 
print(functools.reduce(lambda x,y: x*y, a)) 

#람다이용해 두수의 사칙연산 프로그램v   2k4j5je
Sum= lambda x,y: x+y 
Sub= lambda x,y: x-y 
Mul =lambda x,y: x*y 
Div= lambda x,y: x/y 

import os 
while True: 
    os.system('cls') 
    num1= int(input("첫번째 정수입력 "))
    num2= int(input("두번째 정수입력 "))
    giho = input("계산기호") 
    
    if giho =='+': 
        print("계산결과:",Sum(num1,num2))
    elif giho =='-': 
        print("계산결과:",Sub(num1,num2))
    elif giho =='*': 
        print("계산결과:",Mul(num1,num2))
    elif giho =='/': 
        print("계산결과:",Div(num1,num2)) 
        
#획득자(getter),지정자(Setter), nonlocal 
# 내부함수는 중첩함수에서 함수 클로저 역할도 하지만, 함수 내 자료를 외부로 획득하거나 
# 자료를 수정하는 역할도 한다. 이런 내부함수들은 획득자(Getter), 지정자(Setter)라고 한다. 
# 역활과 필요 요건은 다음과 갇다. 

#획득자 함수: 함수 내부에 생성된 자료를 외부에 반환하는 함수로 반드시 return 명령 갖는다.   
#지정자 함수: 함수 내부에 생성된 자료를 외부에서 수정하는 함수로 반드시 매개변수를 갖는다, 
# 만약 외부함수에서 생성된 자료를 수정할 경우 해당 변수에 nonlocal 명령어를 쓴다. 

#(형식) 
# def 외부함수(): 
#   변수명ㄷ= 값 
#   def 내부함수():  
#       nonlocal 변수명 

#예시) 획득자와 지정자 함수 그리고 nonlocal 명령어를 이용하여 외부함수에서 생성한 자료를 
#외부에서 획득하고 수정하는 예문  

#함수정의 ;
def main_func(num): 
    num_val= num    # 자료를 생성 
    def getter():   # 획득자 함수.. return 
        return num_val
    def setter(value): # 지정자 함수   
        nonlocal num_val#nonlocal명령어 
        num_val = value
        
    return getter, setter #함수 클러저 반환 

#함수 호출 
getter, setter= main_func(100) # num생성  

#획득자 getter호출 
print("num=",getter()) # 획득한 num확인 num=100 

#지정자 setter호출 
setter(200) #num 값 수정 
print("num=", getter()) #num값 수정확인 num= 200  

#함수 장식자(decoration)는 기존 함수 시작부분과 종료부분에 기능을 장식하여 추가해주는
#별도의 함수를 의미함)   
# 즉 현재 살행된 함수를 파라미터로 받아서 내용과 함께 해당 함수를 감싸주는 함수(Wrapping function)#
 
# (형식)
# @함수 장식자 => 사전에 만들어 있어야함. @wrapping함수명  
# def 함수명(): 
#       함수실행문:  

# wrapper함수 
def test(func): 
    def decorated(): 
        print("반가워요~")     #시작부분에 삽입 
        func()              #인수로 넘어온 함수실행
        print("반가웠어~ 안녕") #종료부분 
    return decorated #클로저 함수반환 

# 장식자 적용할 함수 
@test 
def hello(): 
    print("hi",'홍길동^^')
    
#함수호출  
hello()  

#재귀함수(Recursive Function) 
# 함수 내부에서 자신의 함수를 반복적으로 호출하는 함수 
 
# (중요)
# 재귀함수는 반복적으로 호추하기 때문에 반드시 함수 내에 반복의 탈출(exit)조건이 필수
# 재귀함수는 반복적으로 변수를 조금씩 변경하여 연산을 수행하는 알고리즘에서 이용된다. 
# 예제) 팩토리얼(Factorial)계산 등을 사례로 들 수 있다. 

# 예제) 카운트- 1~n 까지 정수를 count(카운트)하는 과정 
def Counter(n): 
    if n==0: 
        print()
        return 0 #종료조건  
    else:
        print(n,end='')
        Counter(n-1) #재귀함수호출  
        
# 함수호출
print("n=0:",Counter(0)) #n=0,0 

# 함수호출
Counter(5)

# [예제-누적합] 
# 1~n까지 정수를 카운트한 값을 누적하여 반환하는 경우
# 재귀함수 정의  
def Adder(n): 
    if n==1: #종료조건 
        return 1 
    else:
        result = n+Adder(n-1) #재귀호출
        print(n, end= '') # 스택영역: 만약 n=5(시작) -> 2 3 4 5 
        return result 
#함수호출
print("n=1:", Adder(1))
print("\nn=5", Adder(5))