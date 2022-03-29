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