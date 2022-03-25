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