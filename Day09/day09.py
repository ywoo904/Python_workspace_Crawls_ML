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
print(bin(234))
