#Builtins함수(내장함수_이미 깔려있는 녀석들) 

#help() #함수,객체에 대한 설명(도움)
#print() #터미널 화면에 결과를 출력
#input() #표준입력으로 받은 결과를 처리 
#sum() #인자값으로 여러개의 숫자를 받아서 합계 함수 
#max() #값들 중에서 가장 큰 수를 반환 
#min() #인자값들 중에서 가장 작은 수를 반환 
#pow() #인자값들 통해서 제곱처리하는 함수 

#내장 함수들은 도움말(Help) -> in module builtins 
# import **: 모듈을 불러오는 명령어  
# import builtins 
# dir(builtins) #내장클래스, 내장함수 목록을 보여줌  

import builtins 
print(dir(builtins))

# 1. abs(x): x를 대상으로 절대값을 반환하는 함수 
print(abs(10)) #10 
print(abs(-10)) #10 
        #list같은 자료형 
# 2. all(iterable): 모든 요소가 True이면 True를 반환(and)
lst1=[1,3,4,7,-9,38] 
lst2=[0,1,2,3,4,5,7]
print(all(lst1)) #True 
print(all(lst2)) #False 0때문에  

# 3.any(iterable): 하나 이상의 요소가 True일때 True를 반환(or) 
lst3=[0,False,'',[  ]]
lst4=[1,False,0,-15.3 ]
print(any(lst3)) #False  
print(any(lst4)) #True 

# 4.bin(number) -> 10진수 정수를 2진수로 변환, 표현식 0b
# oct(number) -> 0o, hex(number)->0x 

# 5. dir(x): 객체 x에서 제공하는 변수,내장함수,내장클래스 목록을 반환
print(dir(lst3))

# 6. eval(expr): 문자열 수식을 인수로 받아서 계산 가능한 파이썬 수식으로 변환 
print(eval("10+20")+30)  #30
# print(eval(10+"20+30")) #문자열이 아니기 떄문에 계산불가
 
# 7.ord(character): 문자열을 인코딩값으로 반환 
# ' ' => 0x20(32) 
# 0 => 0x30(48)
# A => 0x41(65)
# a => 0x61(97)

print(ord('0')) #0x30(48) 
print(ord('a')) #97 
print(ord('A')) #65 
print(hex(ord('가'))) #0xac00(16진수) 

# 8. chr(number): 인코딩값을 다시 문자열로 반환 
print(chr(0x30)) #0 
print(chr(0xac00)) #'가'

#pow(x,y): x에 대한 y의 제곱을 계산하여 반환 
print(pow(2,3)) #8 
print(pow(10,3)) #1000
print(pow(10,-1)) #0.1 
print(pow(-8,-2)) #0.015625 

#10. round(number,자리수): 올림값 처리  
print(round(3.14159)) #3e
print(round(3.14159))

# 11. sorted(iterable): 반복가능한 원소들을 오름차순 또는 내림차순 정렬결과 반환  

# 12. zip(iterable*): 반복가능한 객체와 객체간의 원소들을 묶어서 튜플로 반환 
zi= zip([1,3,5],[2,4,6])
print(list(zi)) #[(1, 2), (3, 4), (5, 6)]

#python의 모듈 및 패키지 사용 
# 모듈(Module)이란? 함수, 변수, 클래스들을 모아놓은 파일  
# (모듈은 만들어놓은 다른 파이썬 프로그램에서 불러와 사용이 가능함) 
# 모듈을 만드는 방법: *.py 확장자를 이용하여 만들 수 있음
# 모듈을 불러오는 방법: import 명령어를 사용하여 모듈을 불러와 사용
# (표준 라이브러리를 불러와 사용할 때에는 import 사용함)  

#시간관련 모듈
import datetime,time #(가공된것/순수날것)

#datetime 모듈은 시간에 대하여 가공된 정보를 처리
a= datetime.datetime.now() #현재시간
print(a) #2022-03-28 21:43:28.347264 

import datetime,time
t= time.localtime()  
s= time.localtime().tm_zone  
print(t) #time.struct_time(tm_year=2022, tm_mon=3, tm_mday=28, tm_hour=21, tm_min=46, tm_sec=59, tm_wday=0, tm_yday=87, tm_isdst=1)
print(s) #EDT 
print(t.tm_year) #2022
print(t.tm_mday) #28 

start = time.time()  
print(start) #1970.01.01.00시를 기점으로 'How many seconds?' 
time.sleep(5) #5초간 작업하던 프로세스 Stop
end = time.time() 
print(end)

# 모듈사용하기
#(형식)
# import 모듈명 => 모듈 내에 있는 모든 함수, 클래스, 변수들을 호출 
# 사용할 때=> 모듈명, 함수(변수,클래스) 
import calc # as를 사용해 별칭으로 호출가능  

a=100 
b=200
c=10 
Sum= calc.Sum(a,b) 
Sub= calc.Sub(a,b)  
Mul= calc.Mul(a,c) 
Div= calc.Div(b,a) 
print("a+b의 결과:",Sum) 
print("a-b의 결과:",Sub) 
print("a*b의 결과:",Mul) 
print("a/b의 결과:",Div) 

calc.Result= (Sum+Sub)-int((Mul/Div)) 
print("((a+b)+(b-a))-((b*c)/(b-a)):",calc.Result)

#[형식2]
#from 모듈 import* 
# => 모듈 내에 있는 모든 변수,함수와 클래스를 호출  
# 모듈내용 사용할경우: 함수(변수,클래스)명을 그대로 사용  
# from calc import * #테스트 용으로 사용하는 경우가 많음... 
 
a=10
b=20
c=30
Sum_re=Sum(a,b) 
Sub_re=Sub(a,b) 
Mul_re=Mul(a,b) 
Div_re=Div(a,b) 
Result= Sum_re+Sub_re+Mul_re+int(Div_re)
print(Sum_re) #30
print(Sub_re) #-10
print(Mul_re) #200
print(Div_re) #0.5
print(Result) #220  

# 패키지 생성순서 
# 1. 패키지로 사용할 폴더를 생성 
# 2. 폴더에 묶어서 사용할 모듈을 저장 
# 3. 패키지를 import 명령어를 사용해 불러옴  
# from 패키지명(폴더명) import 모듈명  
from testpack import Sum,Sub,Multi,Div 

print(Sum.Sum(100,200))
print(Sub.Sub(100,200))
print(Multi.Mul(100,200))
print(Div.Div(100,200)) 

## python파일 입출력 사용 
# -디스크에 파일을 읽어 들이거나 디스크에 파일을 생성하여 저장하는 기능을 의미 
# -많은 양의 데이터를 처리(저장)할 떄에 유용하게 사용됨 
# ex) 홈페이지 이미지, 데이터, 음악, 파일 정보 등을 저장할 떄.. 

# [과정-순서]
# 1. open 함수를 이용하여 파일(객체)을 열기 
# 2. read(읽기) 또는 write(쓰기) 관련 함수를 이용하여 파일에 대해서 작업진행 및 처리하는 단계 
# 3. open으로 열린 파일의 내용을 close함수를 사용하여 닫는다.  

# 1. open함수사용
file = open("day09/data/test_text.txt",mode='w',encoding='utf-8') 
# /data/test_text.txt파일에 대한 fileIO 생ㅅ어
#-"a" => 모드 영역
#open함수 사용 시 모드 설정 값
#r(read-읽기)=>파일 있는경우, 없는 경우 에러
#w(write-쓰기)=>파일 있는경우 있는내용 삭제 후 갱신, 없는경우 생성하고 쓰기진행
#a(append-추가)=>파일 있는경우 마지막에 추가로 쓰기작업, 없는 경우 파일 생성하고 쓰기 
# x  = > 파일 있는경우 생성 에러를 발생, 없는경우 파일을 생성하고 쓰기를 진행  
# Mode에 "+"를 사용하는 경우 추가기능이 사용됨(읽기와 쓰기가 가능함)   
# **모드에 t => text작업, b=> binary작업  
# encoding: 문자설정 

#2. open으로 생성된 내용을 토대로 작업이 진행  
str1= input("파일에 저장할 내용을 입력하세요: ") 
i= file.write(str1) #단위:byte
print("file.write()의 반환 값:",i)

#3. 작업한 파일의 내용을 close()로 종료 
file.close() 


#파일읽기 
# 1.open
rfile= open("day09/data/test_text.txt","r",encoding="utf-8") 
# 2.작업 
readbuffer= rfile.read()  
print(readbuffer)
# 3. close
rfile.close() 

''' 
[QUIZ] 파일명: data/quiz1.txt 
1. 본인 인적사항을 파일에 저장 후 출력하세요 
(이름 나이 주소) 
-당신의 이름: 홍길동
-홍길동님 나이는: 20살 
-홍길동님 주소는: 산골짜기
[출력결과]=> 파일에 저장된 결과를 출력 
홍길동 
20살 
산골짜기
'''
#파일입력 
#file
file= open("day09/data/quiz1.txt",'a',encoding="utf-8")
#work 
name=input("당신의 이름:") 
age= input(f"{name}님의 나이는:") 
address=input(f"{name}님의 주소는:")
file.write(name+"\n"+age+"\n"+address+"\n")
#close 
file.close() 

#파일출력 
rfile= open("day09/data/quiz1.txt",encoding="utf-8")
buf= rfile.read() 
print(buf)  
rfile.close() 

#[예제2]readline()=> 데이터를 읽을때 "\n"을 기준으로 읽어들이는 함수 
rfile2= open("day09/data/quiz1.txt",'r',encoding="utf-8") 
while True: 
    readbuffer= rfile2.readline()
    if readbuffer=="": # 문자열의 마지막을 의미 
        print("\n더이상 값이 존재하지 않습니다.")
        rfile2.close() 
        break 
    print(readbuffer,end='') 
 
#[예제3] readlines()=> \n을 기준으로 데이터를 읽어들이는 함수,
#읽어들인 문장들은 리스트에 저장하는 함수  
rfile3= open("day09/data/quiz1.txt",encoding="utf-8") 
buf3= rfile3.readlines() 
print(buf3,type(buf3))
rfile3.close() 

#문자열리스트에 "\n"을 제거하여 저장하세요 
for i in range(len(buf3)): 
    buf3[i]= buf3[i].strip('\n')
    print(buf[i]) 
print(buf3,type(buf3)) 

#[예제4] ord() -> 문자를 인코딩 값으로 출력 
# chr() -> 인코딩 값을 문자로 출력ㄷ
print(hex(ord('안')))
print(hex(ord('녕')))
print(hex(ord('하')))
print(hex(ord('세')))
print(hex(ord('여')))
print(hex(ord('1')))
print(hex(ord('a')))

print(chr(0xc548))
print(chr(0xc155))
print(chr(0xc558))
print(chr(0xc138))
print(chr(0xc5ec))
print(chr(0x31))
print(chr(0x61))

#[예제5]문자의 암호화(한글자)
readstr, content= "",""  
key=100 #암호화연산을 위한 값
choice= input("1.파일저장\n2.파일불러오기\n번호선택>>>") 
fileName= input("파일명 입력:")

if choice==1: 
    content= input("단일문자 입력: ") 
    #open 
    sfile = open("day09/data/"+fileName+".txt",'w',encoding="utf-8")
    #work 
    chNum= ord(content) 
    chNum= chNum + key 
    content= chr(chNum)
    sfile.write(content)
    #close
    sfile.close() 
    
elif choice==2:
    rfile = open("day09/data"+fileName,"r",encoding="utf-8")
    readstr= rfile.read() 
    chNum= ord(readstr)
    chNum= chNum-key 
    readstr= chr(chNum) 
    print("파일에 저장된 값:",readstr) 
    rfile.close() 

# [문제1]
# 위 예제를 이용해 문자열을 암호화해주세요 
#단일문자만 저장가능 
#문자열을 암호화하여 파일에 저장할 수 있도록 코드를 수정 
#반대로 암호화된 문자열을 복호화하여 화면에 출력할 수 있도록 코드를 수정
import os
readstr, savestr,printstr= "","","" 
key=100 
while True:
    os.system('cls')
    choice= input("1.파일저장\n2.파일불러오기\n0.종료\n번호선택>>>") 
    fileName= input("파일명 입력: ")
    
    if choice== '1': 
        sfile=open("Day09/data/"+fileName,"w",encoding="utf=8")  
        contents= input("문자열 입력: ")
        for i in contents: 
            chNum= ord(i)  
            chNum +=key 
            savestr +=chr(chNum)  
        sfile.write(savestr)
        sfile.close() 
            
    elif choice== '2': 
        rfile=open("Day09/data/"+fileName,"r",encoding="utf=8") 
        readstr= rfile.read() 
        for i in readstr: 
            chNum=ord(i) 
            chNum-= key
            printstr+= chr(chNum) 
        print("파일에 저장된 값:",printstr) 
        rfile.close() 
        os.system('pause')
        
    elif choice=='0': 
        print("프로그램을 종료합니다.") 
        break 
    else: 
        print("입력값 오류, 다시 입력하세요") 
        os.system('pause')
    

#문제2 
# # 위 예제를 이용해 문자열을 암호화해주세요 
#단일문자만 저장가능 
#문자열을 암호화하여 파일에 저장할 수 있도록 코드를 수정 
#반대로 암호화된 문자열을 복호화하여 화면에 출력할 수 있도록 코드를 수정ㄷ
import os
readstr, savestr,printstr= "","","" 
key=10
while True:
    os.system('cls')
    choice= input("1.파일저장\n2.파일불러오기\n0.종료\n번호선택>>>") 
    fileName= input("파일명 입력: ")
    
    if choice== '1': 
        sfile=open("Day09/data/"+fileName,"a",encoding="utf=8") 
        while True: 
            contents= input("문자열 입력: ")
            for i in contents: 
                chNum= ord(i)  
                chNum +=key 
                savestr +=chr(chNum)  
            savestr += "\n" #줄바꿈 
            sel= input("문자열 입력을 계속하겠습니까?(Y/N)") 
            if sel== 'n': 
                sfile.write(savestr)
                sfile.close() 
                break 
            
    elif choice== '2': 
        rfile=open("Day09/data/"+fileName,"r",encoding="utf=8") 
        
        while True:
            readstr= rfile.readline()
            if readstr =="": 
                rfile.close()
                break
            for i in readstr: 
                chNum=ord(i) 
                chNum-= key
                printstr+= chr(chNum) 
            printstr +="\n"
        print("파일{fileName}에 있는 내용\n{printstr}") 
        os.system('pause')
            
        print("파일에 저장된 값:",printstr) 
        rfile.close() 
        os.system('pause')
        
    elif choice=='0': 
        print("프로그램을 종료합니다.") 
        break 
    else: 
        print("입력값 오류, 다시 입력하세요") 
        os.system('pause')
    
# open()의 모드에 "+"옵션 사용하기 
fileName= input("파일명 입력: ")
file= open(fileName,"r+",encoding="utf-8")
readstr= file.read() 
print(readstr,end="") 
writestr= input("\n문서에 추가할 내용을 입력하세요") 
file.write(writestr) 
file.close() 

#모드옵션 
#t=> 텍스트(문서)=> 생략가능 
#b=> 바이너리(이진데이터) 

#[문제] file입출력을 이용하여 "특정파일"을 복사하는 프로그램 코드를 작성하세요 
#복사할 대상(원본): Day09/data/download.png
#복사할 위치(복사본): Day09/data/download_copy.png 
source= input("복사할 대상(원본)")
destination = input("복사할 위치(복사본)")
#open 
rfile=open(source,"rb")
wfile=open(destination,"wb")
#work 
rbuffer = rfile.read() 
i= wfile.write(rbuffer)
if i != 0 or i != -1: 
    print("복사를 성공적으로 마쳤습니다. 파일크기는 {:,} bytes입니다.".format(i)) 
else: 
    print("복사가 완료되지 않았습니다. ") 
#close
rfile.close() 
wfile.close() 

#예외처리_프로그램에서 벌어지는 예외적 상황(Error들)

#예)
#-파일을 읽고자 할때 그 파일이 존재하지 않는경우(FileNotFound)
#-어떤 값을 0으로 나누고자 할때 (ZeroDivision) 
#-배열의 인덱스 범위를 벗어났을경우 
#-사용자의 요구대로 진행이 되지 않았을경우 
# (예외처리형식)
#try: 
#   예외처리 검증구문 
#   예외처리 검증구문 
# except(예외처리-에러코드):
#   예외처리 검증구문 
#   예외처리 검증구문 
# finally: 
#   마지막 실행할 코드 

# [예제1] 검증내용은 두수를 나누기 할때  
try:
    num1= int(input("첫번째 정수:"))
    num2= int(input("두번째 정수:")) 
    Div= num1/num2
    print("나눗셈 결과:",Div)
except ValueError: 
    print("정수값 입력하세요") 
except ZeroDivisionError: 
    print("숫자0으로 나눌 수 없어요") 
print("에외처리 이후 프로그램 진행 ")

# [예제2] try~except~else구문
# try: #예외검증 
#   예외검증문장1 
#   예외검증문장2 
# except (예외코드): #예외발생 시 동작 
#   예외발생시코드 
#   예외발생시코드 
#...
# else:         #예외 발생 안한 경우 실행 
#   예외 발생하지 않은 경우 코드1 
#   예외 발생하지 않은 경우 코드2 

try: 
    num= int(input("수입력:")) 
except ValueError:
    print("정수만 입력하세요!") 
else: 
    print("입력값출력{}- 예외처리 안된경우 실행".format(num))
    
# 예제3] 파일 관련 예외처리(파일없는 경우) 
fileName= input('파일명:') 
try: 
    file=open(fileName,"r",encoding="utf-8") 
    buf= file.read() 
    print(buf)
except FileNotFoundError: 
    print("지정한 파일이나 디렉터리가 존재하지 않습니다.") 
except Exception as e: 
    print(e,"에러가 발생했습니다. ") 
else: #finally => 항상 실행 
    file.close()
    print("문제없이 잘 실행했습니다. ")
    
# 문제] 나이를 입력받는 프로그램을 만들때에 잘못된 값을 입력시 에외처리 만드세오 
# -입력값 에러: ValueError => 소숫점 이하 문자, 문자를 입력  
# -입력값이 0보다 작은 경우, 
#   강제로 Exception 작업을 해야함, 
#   => raise Exception("예외사항")
try: 
    num= int(input("나이입력:")) 
    
    if num<0:
        raise Exception("예외사항")
    
except ValueError:
    print("양의정수만 입력하세요!") 
except Exception as e: 
    print(e,"0보다 작은 나이는 존재하지 않습니다.")
else: 
    print("입력값출력{}- 예외처리 안된경우 실행".format(num)) 
finally:
    print("프로그램을 종료합니다.")