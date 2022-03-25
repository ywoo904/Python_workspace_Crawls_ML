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

#[QUIZ]  
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
    if not num %3:
        return f"{num}은 3의 배수입니다."
    else: 
        return f"{num}은 3의 배수가 아닙니다."
    
txt= int(input("숫자를 입력하세요"))
result= threepower(txt)
print(result)


#3: 계산기를 입력,출력,연산기능으로 나눠서 실행되게 작성해주세요
# 입력 => 계산처리 => 출력

def cal(num1,num2,giho): 
    if giho =='+':  
        return num1+num2
    elif giho =='-':  
        return num1-num2
    elif giho =='*':  
        return num1*num2
    elif giho =='/':  
        return num1/num2
    
def output(num1,num2,giho,result): 
    print(num1,giho,num2,"=",result)

def Input():
    num1,giho,num2= int(input("첫번째 정수입력: ")) \
    ,input("계산기호입력(+-*/):"),int(input("두번째 정수입력:"))
    result= cal(num1,num2,giho) 
    output(num1,num2,giho,result)

#메인: 
Input()     
    

#4. 예제 거꾸로 수를 반환하는 함수를 계산, 출력기능으로 나눠서 작성해주세요.  
def backwards(num): 
    list= [] 
    for i in range(len(str(num))): 
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
#위는 내가한거 

def reverseCode(result): 
    tmp, su= 0,0
    while True: 
        tmp= result%10 
        result= result//10 
        su= (su+tmp)*10 
        if not result: 
            return su//10 

def display(): 
    result, su=0,0
    result=int(input("정수입력:")) 
    su= reverseCode(result) 
    print("변환전값:{}, 변환후값:{}".format(result,su)) 
    
#메인 
display() 

#예제: 친구이름 관리를 함수로 기능을 나눠서 작성해주세요 
# 1. 친구목록보기 
# 2. 친구추가 
# 3. 친구삭제 
# 4. 친구수정 
# 0. 종료  
def fr_list(lst): #친구목록보기
    print("="*15,"친구목록보기","="*15)
    if lst !=[]:
        for i in range(len(lst)):
            print(f"{i}:{lst[i]}")
    else:
        print("등록된 친구가 없습니다.")
def fr_add(lst): #친구추가 
    name=input("등록할 이름입력:")
    lst.append(name)
    
def fr_del(lst): #친구삭제
    name=input("삭제할 이름입력:")
    if name in lst:
        lst.remove(name)
    else: 
        print("삭제할 친구가 없습니다.")
def fr_mod(lst): #목록수정
    name = input("수정할 친구이름 입력")
    if name in lst: 
        idx=lst.index(name)
    else: 
        print("수정할 친구가 없습니다.")
        return 
    name_mod= input("변경이름 입력하세요:")
    lst[idx]= name_mod

#main 
import os
lst=[]
while True:
    print("="*15,"친구관리 프로그램","="*15) 
    print("1.친구목록보기")
    print("2.친구추가")
    print("3.친구삭제") 
    print("4.친구수정")
    print("0.종료")
    sel=input("메뉴를 선택하세요 [0-4] ") 
    if sel== '1': 
        fr_list(lst)
        os.system('pause')
    elif sel=='2':
        fr_add(lst) 
        os.system('pause')
    elif sel=='3':
        fr_del(lst)
        os.system('pause')
    elif sel=='4': 
        fr_mod(lst)
        os.system('pause')
    elif sel=='0':
        print("프로그램을 종료합니다.")
        break
    else:
        print("메뉴선택이 잘못됬습니다.")
        os.system('pause')
        
#문제) 알바시급 프로그램 작성 (default 인자값 사용) 
# 시급: 8500원 하루 8시간 한달 30일 (기본값) 
# 다음과 같이 출력되게 
# <<시급계산 프로그램>> 
# 1. 기본급
# 2. 일한 날짜 입력 
# 번호입력 >> 


#function
def alba(day=30):
    time=8; price=8500
    re=time*price*day
    return re 
#main
def display(): 
    print("<<시급계산프로그램>>")
    print("1.기본급")
    print("2.일한 날짜입력")
    sel=int(input("번호입력>>"))
    if sel==1: 
        result= alba()
    elif sel==2: 
        day= int(input("일한 일 수 입력:"))
        result= alba(day)
    print("당신의 급여는{:,}원 입니다.".format(result))
display() 

#인자값 처리방식1 => 연속된 자료를 처리하는 함수의 인자처리방식

#예제: 
def pr8(a,b,c):
    print(a,b,c)
    
#메인: 
pr8(10,20,30) # 10 20 30 

# "*"를 이용하여 리스트 또는 튜플과 같은 자료를 연속된 인자값으로 처리 
# 리스트 또는 튜플의 변수값을 받아서 unpacking방식으로 인자를 전달 
x=[100,200,300]
y= [10,20]
z= 1,2,3,4 
pr8(*x) # 100 200 300 
pr8(*y,30) # 10 20 30 
pr8(*z) # TypeError 

# *를 이용하여 연속된 자료(리스트,튜플)에 데이터를 인자로 전달이 가능하나 인자의 개수와 전달되는 
# 자료의 개수는 같아야 한다. 

#인자값 처리방식 2= > 가변인자값 처리 ... 
# 고정인자 => 인자값을 반드시 정해진 값으로 1:1로 인자를 전해야하는 인자(일반) 
# 가변인자 => 인자값을 정해진 개수로 전달하지 않고, 가변적으로 전달가능한 인자 
# 가변인자 설정은 함수 정의시에 매개변수(인자)앞에 "*"를 사용한다. 

#전달된 인자값들의 합을 구하는 예제: 
def sum_func(*par): 
    result= 0 
    print(par,type(par)) #전달된 인자값 처리 방식 
    for su in par: 
        result+=su
    return result
def display():
    sum=0
    sum=sum_func()
    print(sum)
    sum= sum_func(10,20,30)
    print("인자가 세개(10,20,30)인 경우 결과:",sum)
    sum= sum_func(10,20,30,40,50) 
    print("인자가 다섯개(10,20,30,40,50)인 경우 결과",sum) 
    
display() 

# 주의) 인자값 처리함에 있어 고정인자와 가변인자를 동시에 사용하는 경우, 
# 고정인자를 먼저 처리하도록 한다. 즉 가변인자는 마지막에 사용되게 해야한다. 
# 예제) 딕셔너리 자료형을 받아서 처리하는 함수 
def dic_func(**par): 
    print(par,type(par)) 
    for k in par: 
        print("{}:{}".format(k,par[k]))
#메인
dic_func(피카츄='1마리',파이리='2마리',꼬부기='없음',라이칸='1') 

dic= { 
      'sep': '-',
      'end': '\n\ntest'
} 
lst=['test1','test2','test3','test4'] 

print('test','test','test',**dic) #test-test-test
print('test','test','test',sep='-',end='\n\ntest') #testtest-test-test
print(*lst,**dic) # testtest1-test2-test3-test4