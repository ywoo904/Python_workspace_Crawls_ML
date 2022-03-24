'''
아래의 내용을 토대로 프로그램을 작성하세요 
1. 다음과 가은 메뉴와 가격을 key 와 value로 사용하여 
사전형 자료를 만들어보세요(변수명은 menu)
칼국수 6000원 
비빔밥 5500원 
돼지국밥 7000원
돈까스 7000원  
김밥 2000원 
라면 2500원 

2, 위에서 만든 사전형 자료 menu변수에서 가격이 6000 미만에 해당하는 메뉴와 가격을 출력하는 
코드를 작성하세요  

3. 사용자 입력으로 메뉴와 가격을 입력받아 menu 변수에 자룔르 추가할 수 있도록 하시오  
(동일한 메뉴는 가격만 변경) 

4.메뉴를 자동으로 선택하여 출력하게 만들어보세요 
'''
menu = {
    '칼국수': 6000,
    '비빔밥':5500,
    '돼지국밥':7000,
    '돈까스':7000,
    '김밥':2000,
    '라면':2500 } 

for me in menu: 
    if menu[me]< 6000: 
        print(f"{me}:{menu[me]}원")
        
add_menu= input("추가메뉴를 입력하세요:") 
add_price=int(input("메뉴가격을 입력해주세요:"))
if add_menu in menu: 
    menu[add_menu] = add_price
else: 
    menu.update({add_menu:add_price})
    
sel= input("메뉴를 자동으로 출력하겠습니까?(Y/N)")
if sel =='Y' or sel != 'N':
    for me in menu: 
        print(me,menu[me],'원') 

## set 클래스 
# 여러개의 자료를 비순서로 적재하는 가변길이 비순차 자료형 
# 변수 = {값1,값2,값3...} 
# 중복허용 x, 순서가 없기 때문에 index 사용불가
# 객체에서 제공하는 함수를 이용하여 추가, 삭제 및 집합연산 등이 가능함
# 1) 중복불가 
se = {1,2,3,4,1} # 숫자의 경우에는 정렬표시됨  
print(len(se)) #길이 카운트에 중복허용x 
print(se) #출력에 중복허용x 

st= set("hello") #set() : 셋타입을 생성하는 함수
print(len(st)) 
print(st)

#  2) 요소반복 
for d in se: 
    print(d, end=' ')
print()  

for s in st: 
    print(s, end=' ') 
print() 

# 3)집합관련함수 
# -union([set타입자료]): 합집합 
# -difference([set타입뺄자료]): 차집합 
# -intersectino([set타입자료]): 교집합
# - add(): 집합에 값을 추가하는 함수   
# -discard
se = {1,2,3,4,1}
se2={2,4,6,8}
print(se.union(se2))        # {1,2,3,4,5,6}
print(se.difference(se2))   # {1,3}
print(se.intersection(se2)) # {2,4}
se3= {1,3,5} 
se.add(se3)  #원소를 추가  
print(se )

st2 = set('world')# 
print(st.union(st2)) 
print(st.difference(st2)) 
st.add('test')
print(st) 

#값의 타입은 상관하지 않는다 
lst= ['test','user','sever','data'] 
print(set(lst)) 

#set을 사용하는 예시: 중복된 원소를 제거 

#python의 문자열
# : 파이썬의 사용하는 문자열 처리 
#특징 
# 1) 인덱싱을 이용한 참조가능 
string = 'python string'
#         01234567891011
print(string[0]) #p 
print(string[7]) #s 
print(string[-1]) #g 
# 2) 슬라이싱을 이용한 참조  
print(string[:6])
print(string[0::2]) #pto tig 
# 3) 문자열 반복문(for) 
st= "python string for"
for x in st: 
    print(x,end=" ") 
print() 

#문자열 함수
#-find(str): 문자열에서 특정 문자열을 찾아서 해당 문자의 index값을 반환
#-count(str): 문자열에서 특정 문자열을 찾아서 해당 문자열의 수를 반환 
#-lower(): 문자열에서 영문 대문자를 소문자로 변경하여 반환 
#-upper(): 문자열에서 영문 소문자를 대문자로 변경하여 반환  
#-strip(): 문자열에서 양쪽 공백 또는 문자를 제거반환 
#-lstrip(): 문자열에서 왼쪽 공백 또는 문자를 제거하여 반환  
#-rstrip(): 문자열에서 오른쪽 공백 또는 문자를 제거하여 반환  
#-replace(old,new): 문자열에서 왼쪽(old)문자열을 찾아서 오른쪽(new)로 변경 
#-split(): 문자열을 특정문자 기준으로 분리 -> 반환값을 리스트 

print(help('str')) 

#find예제 
st= 'python string' 
#    0123456789... 
print(st.find('string'))#시작인덱스 7을 반환  
# find(str,시작인덱스,끝인덱스)  
print(st.find('t')) #2
print(st.find('t',3)) #8 
print(st.find('t',9)) #-1(문자열 찾지 못함)
# find()가 문자열을 찾지 못한 경우의 반환값: -1

# count() 
st= 'python string' 
print(st.count('t')) #2 
# count(str,시작인덱스,끝인덱스) 
print(st.count('t', 6))  #1

# lower() 대문자를 소문자로 
st= 'PYTHON STRING'
print(st.lower()) #python string
print(st)  #PYTHON STRING (변수원본을 수정하지 않음) 
st1= st.lower() #수정본을 따로 변수로 저장해줘야함 
print(st1)

# upper() 소문자를 대문자로  
st = 'python string' 
print(st.upper())
st2= st.upper() 
print(st2)

# strip (): 양쪽의 인자로 전달받은 문자열을 제거  
# 인자값이 없는 경우에는 공백을 제거  
st = '      python string        ' 
print(st)
print(f"[{st}]") 
st1= st.strip() 
print(st1) 
 
#lstrip()
st2=st.lstrip() 
print(f"[{st2}]")

#rstrip()
st3=st.rstrip()
print(f"[{st3}]")

# replace (old new) 
st= 'python string' 
st1= st.replace('string','문자열') 
print(st1)      #python 문자열  