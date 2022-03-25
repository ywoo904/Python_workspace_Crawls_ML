#함수(Function): 프로그램에서 사둉할 기능을 미리 정의해서 구현한것  
#또 다른 의미의 프로그램 내의 작은 프로그램 

#python 함수정의(생성) 
# def 함수이름([인자list]):
#   함수기능에 대한 정의1
#   함수기능에 대한 정의2
#   함수기능에 대한 정의3
#   ... 

# -함수 사용에 있어서 설명이 필요한 경우 함수 내부의 주석을 사용하여 기술(여러줄)
# -함수 만들 때 함수의 기능을 알 수 있는 이름으로 정의 권장  
# -미리 만들어 놓은 함수 호출 시에는,"함수이름([인자])"로 호출
# -정의 생성된 함수의 반환값이 있는 경우, "return" 명령어를 사용
# -함수의 반환값이 있을 수도, 없을 수도 있음. 있는 경우 return 
# -없는 경우 "return"은 함수가 종료
# -함수에 필요하면 인자값을 전달할 수 있다.
# -전달된 인자값은 함수 정의시에 만든 "매개변수"에 그 값이 저장된다.
# -이후 함수 정의부에서 해당 내용을 가지고 구동

#예제1] 사용자가 입력한 값을 출력하는 함수구현 

#함수정의 
def pr():
    txt= input("입력값:") 
    print()
    print("입력한 내용은:",txt) 
#함수호출
pr() 

#실습-입력값을 받아서 사칙연산하는 프로그램 함수를 사용.
# 그 함수 이름은 calc()로 구현해보세요  
# (메인에서 calc()호출하면 모든 동작이 가능하도록 설정)

def cal(): 
    
    num1= int(input("첫번째 수 입력:")) 
    num2= int(input("두번째 수 입력:"))
    result= 0 
    cal= int(input("1.더하기 2.뺴기 3.곱셈 4.나눗셈 >>"))
    if (cal==1):
        result= num1+num2
        print("정답은:",result)
    elif (cal==2):
        result= num1-num2
        print("정답은:",result)
    elif (cal==3):
        result= num1*num2
        print("정답은:",result)
    elif (cal==4):
        result= num1/num2
        print("정답은:",result)   
#함수호출 
cal()  
    
#예제2] 함수의 인자값 사용- 사용자가 입력한 값을 출력하는 함수를 구현  
#함수정의 
def pr2(str1): 
    print("입력한 내용은:", str1) 
#메인 
txt= input("입력:")
pr2(txt)


#실습: 입력값을 받아서 사칙연산하는 프로그램 함수를 사용하여 동작하게 만드세요  
# 함수명은 "calc([문자열인자값])"로 사용하세요  
#함수정의 
def calc(calc):
    if '+' in calc: 
        num1,num2=calc.split('+')
        num1= int(num1); num2= int(num1); 
        print("계산 결과는:",num1+num2)
    elif '-' in calc: 
        num1,num2=calc.split('-')
        num1= int(num1); num2= int(num1); 
        print("계산 결과는:",num1-num2)
    elif '*' in calc: 
        num1,num2=calc.split('*')
        num1= int(num1); num2= int(num1); 
        print("계산 결과는:",num1*num2)
    elif '/' in calc: 
        num1,num2=calc.split('/')
        num1= int(num1); num2= int(num1); 
        print("계산 결과는:",num1/num2)
    else:
        print("수식입력이 잘못됬습니다.\n다시 입력해주세요.")
#함수메인 
import os 
while True: 
    os.system('cls')
    txt=input("계산할 수식을 입력해주세요:[ex)5+5]")  
    calc(txt) #함수호출부분 
    sel = input("계속하시겠습니까?(Y/N):") 
    if sel== 'n':
        break
print("프로그램 종료")

#예제3] 함수의 인자값 사용- 사용자가 입력한 값을 출력하는 함수구현 
# 사용자로 부터 입력받은 값을 인자값으로 처리하는 함수  
# 함수에 return을 사용하여  반환값을 처리하는 예제 

#함수정의 
def pr3(str1):
   '''함수설명: 연산결과 후에 반환값을 전달하는 함수 ''' 
   return "입력한 문자열"+str1
   
#메인 
txt= input("입력:")
print()
pr_out= pr3(txt)  
print(pr_out)

# 실습] 위 내용을 토대로 계산결과를 반환값으로 처리하는 함수로 변환 
def pr4(calc): 
    '''함수설명: 사칙연산숫자를 받아 계산하는 함수프로그램''' 
    if '+' in calc: 
        num1,num2=calc.split('+')
        num1= int(num1); num2= int(num1); 
        result= num1+num2 
        return result
    elif '-' in calc: 
        num1,num2=calc.split('-')
        num1= int(num1); num2= int(num1); 
        result= num1-num2 
        return result
    elif '*' in calc: 
        num1,num2=calc.split('*')
        num1= int(num1); num2= int(num1); 
        result= num1*num2 
        return result
    elif '/' in calc: 
        num1,num2=calc.split('/')
        num1= int(num1); num2= int(num1); 
        result= num1/num2 
        return result 
    else:
        return 0 
#메인 
import os

while True:
    os.system('cls')
    txt= input("수식을 입력하세요 ex)5+5 >>>")
    result=pr4(txt)
    print(type(result))
    if result: 
        print("계산결과는:",result) 
    else: 
        print("수익입력이 잘못됬습니다. \n 내용을 다시 확인해주세요.")
    sel = input("계속하시겠습니까?(Y/N):") 
    if sel== 'n':
        break
print("프로그램 종료")

#두 수에 대한 한번에 계산식을 입력받아서 결과를 출력하는 코드를 ㅣㅇ용
# 사용자가 계산식을 입력. 이것을 이용해서 처리 
# calc()가 인자값으로 두 정수와 계산식(기초: + - * /)을 인자로 받아 처리하는 함수를 만들어 동작 

#함수정의
def calc(num1,num2,giho): 
    '''함수설명: 숫자2개, 사칙연산을 받아 계산하는 함수프로그램''' 
    if '+' in giho: 
        return num1+num2 
    elif '-' in giho: 
        return num1-num2 
    elif '*' in giho: 
        return num1*num2 
    elif '/' in giho: 
        return num1/num2 
    else: 
        return 0 

#메인 
import os

while True:
    os.system('cls')
    txt= input("수식을 입력하세요 ex)5+5 >>>")
    if '+' in txt:
        num1,num2=txt.split('+')
        num1= int(num1); num2= int(num1); giho='+';
    elif '-' in txt:
        num1,num2=txt.split('-')
        num1= int(num1); num2= int(num1); giho='-';
        
    elif '*' in txt:
        num1,num2=txt.split('*')
        num1= int(num1); num2= int(num1); giho='*';
        
    elif '/' in txt:
        num1,num2=txt.split('/')
        num1= int(num1); num2= int(num1); giho='/';
    else: 
        print("수익입력이 잘못됬습니다. \n 내용을 다시 확인해주세요.")
        os.system('pause')
        continue
    
    result= calc(num1,num2,giho) #함수호출
    if result !=0: #0인 경우 수식오류 
        if type(result) is not float: 
            print("계산결과는:",result)
        else: 
            print("계산결과는: {:.2f}".format(result))
    sel= input("계속 하시겠습니까?(Y/N):") 
    if sel== 'n':
        break
print ("프로그램 종료")


## 함수 인자 기본값(default) 설정 
# default란? 입력 인자값이 없는 경우에 기본적으로 적용되어지는 값을 의미함. 

# 형식) 
# def 함수이름(param1,param2=1): 
#       함수정의문1 
#       함수정의문2
#  이렇게 정의된 함수가 있는 경우,param2는 기본값으로 '1'을 가지고 있는 것임. 
# 즉, 인자값으로 param2에 전달되지 않아도 기본값으로 '1'을 가진다. 

# 예제4] 함수 인자의 기본값 설정(인자1) 
def pr4(par1=10): 
    print(par1)
    
#메인 
pr4(10) #10 덮어쓴다 
pr4(20) #20 덮어쓴다 
pr4(3) #3 덮어쓴다 
pr4() #10 기본값인 10을 사용 

# 인자를 2개 가진 경우(모두 default인자인 경우)
def pr5(par1=10, par2=20): 
    print(par1,par2)  
    
# 메인 
pr5(100,200) #100 200 
pr5(100)  #100 20
pr5(200)  #200 20
pr5(par2=200) #10 200 
pr5()     #10 20 

# 인자가 2개 이상, 기본값이 1개인 경우 
def pr6(par1,par2=20): 
    print(par1,par2)
    
# 메인 
pr6(100,200) #100 200 
pr6(100)  #100 20
pr6(200)  #200 20
# pr()    # TypeError: pr6() missing 1 required positional argument: 'par1'
#인자는 반드시 전달되어야 한다. 

# 인자의 기본값이 맨 앞에 있는 경우...
def pr7(par1=10, par2): #SyntaxError: non-default argument follows default argument
    print (par1,par2)   #기본값 뒤에는 일반 인자가 존재하면 안됨. Default값은 무조건 뒤로 뺴라 
pr7()

#[ QUIZ]  
#1. 짝, 홀수를 구분하는 함수를 작성하세요 
def evenodd(num):
    if num %2==0: 
        return f"{num}은 짝수입니다." 
    else: 
        return f"{num}은 홀수입니다"

txt=int(input("숫자를 입력하세요:"))
result= evenodd(txt) 
print(result)

#2. "3의 배수를 판별하는 함수를 작성해주세요" 

def threepower(num):
    if num %3==0:
        return f"{num}은 3의 배수입니다."
    else: 
        return f"{num}은 3의 배수가 아닙니다."
txt= int(input("숫자를 입력하세요"))
result= threepower(txt)
print(result)


#3: 계산기를 입력,출력,연산기능으로 나눠서 실행되게 작성해주세요
# 입력 => 계산처리 => 출력

def cal(txt): 
    if '+' in txt: 
        num1,num2=txt.split('+')
        num1=int(num1); num2= int(num2);
        result= num1+num2 
    if '-' in txt: 
        num1,num2=txt.split('-')
        num1=int(num1); num2= int(num2);
        result= num1+num2 
    if '*' in txt: 
        num1,num2=txt.split('*')
        num1=int(num1); num2= int(num2);
        result= num1*num2 
    if '/' in txt: 
        num1,num2=txt.split('/')
        num1=int(num1); num2= int(num2);
        result= num1/num2 
    return result

txt=input("입력: 계산할 수식을 입력하세요.")
result= cal(txt) 
print("출력: ",result)

#4. 예제 거꾸로 수를 반환하는 함수를 계산, 출력기능으로 나눠서 작성해주세요.  
def backwards(num): 
    list= [] 
    for i in range(len(str(num))): #i= 0,1,2,3 # 1234->4321 
       #3뽑기 1234%100= 34 34//10= 3
       #2뽑기 1234%1000= 234 234//100=2 
       #1뽑기 1234//1000
        if i ==0:
          list.append(num%10)
        elif i>0 and i < len(str(num))-1:
          list.append(num%10**(i+1)//10**i)
        elif i== len(str(num))-1: 
          list.append(num//10**i) 
    return list

txt=int(input("거꾸로 출력할 숫자를 입력하세요"))
result=backwards(txt) 
print(result)
