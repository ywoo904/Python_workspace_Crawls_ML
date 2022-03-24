# count(value): 특정 값의 개수를 출력
lst1= [1,2,3,4,5,6,2,8] 
su=lst1.count(2) 
print(lst1) 
print("2의 값을 가진 맴버의 개수: ",su) 

#index(value): 특정값의 인덱스를 반환  
lst1= [1,2,3,2,5,6,2,8]  
#index=[0,1,2,3,4,5,6,7]
idx = lst1.index(2,7) 
#'7'번 인덱스 이후의 2 value값 가지고 있는 인덱스 반환해라  
print("idx의 값을 확인: ", idx) 

#reverse(): 리스트 멤버의 순서를 반전(정렬x) 
lst1=[9,10,3,2,6,1,7,8,4,5]
print("reverse() 사용전: ", lst1)  
lst1.reverse()
print("reverse() 사용후:", lst1)

# sort(): 리스트를 정렬하는 함수  
#      -오름차순(짝은->큰)=> reverse=False(생략:기본값)
#      -내림차순(큰->작은)=> reverse=True
lst1= [5, 4, 8, 7, 1, 6, 2, 3, 10, 9]
lst1.sort() #그냥하면 오름차순 정렬 
print("1st1을 오름차순 정렬:",lst1) 
lst1.sort(reverse=True)  
print("lst1을 내림차순 정렬:",lst1)

# sort사용 시 주의사항
# 1. 숫자형식 또는 문자형식은 분리해서 정렬해야 한다. 
# 2. 정수와 실수는 같은 숫자이기 떄문에 정렬이 가능하다.  
# 3. 정렬된 리스트를 새롭게 만들고 싶은 경우, sorted()를 사용 
lst2 = sorted(lst1) 
print(lst1,id(lst1))
print(lst2,id(lst2))

#ASCI 코드의 벨류값대로 오름차순이 일어난다 
lst3= sorted("I am a student".split()) #split()은 문자열을 띄어쓰기로 분류해 list로 반환  
print(lst3) # 결과값: ['I', 'a', 'am', 'student']

lst4= sorted ("I am a student".split(),key=str.lower) #정렬 기준을 모두 소문자로 삼겠다. 
print(lst4) # 결과값: ['a', 'am', 'I', 'student']

#split() 문자열을 분리하는 하뭇 
# "()"안에 아무것도 넣어주지 않으면, 공백(스페이스, 탭, 엔터 등)을 기준으로 문자열을 나눔 
# 만약 split(';')을 사용하면 ;를 기준으로 문자열을 나눔  

# Copy기능
# -shallow copy: 서로 다른 변수가 같은 위치에 있는 데이터를 가르키는 경우 
# -deep copy: 두개의 변수가 별도의 공간을 가리키는 경우 
lst1= [1,2,3,4,5] 
lst2= lst1 
print("lst1의 값:",lst1,"\tlst1의 주소값:", id(lst1))
print("lst2의 값:",lst2,"\tlst2의 주소값:", id(lst2)) 
lst1[1]='a' 
print(lst1)
print(lst2)

#(예) deep copy (참조하는 데이터의 위치가 다르다 )
lst1=[1,2,3,4,5] 
lst2= list(lst1) #list()는 새로운 리스트를 생성하는 매서드  
print(lst1,id(lst1)) # [1, 2, 3, 4, 5] 4329009920
print(lst2,id(lst2)) # [1, 2, 3, 4, 5] 4329861440 

# deepcopy() 복사기능을 제공하는 copy모듈을 불러서 사용 
import copy  
lst1=[1,2,3,4,5] 
lst2= copy.deepcopy(lst1) #deepcopy() 
lst3=lst1 #shallow copy

'''
QUIZ1: 리스트 초기값 [30,20,10] 설정 후 아래와 같이 출력되도록 코드작성
현재리스트: [30,20,10] 
append(40)한 후의 리스트: [30,20,10,40] 
pop() 으로 추출한 값: 40
pop() 후의 리스트: [30,20,10] 
sort() 후의 리스트: [10,20,30] 
reverse() 후의 리스트: [30,20,10 ]
'''
list=[30,20,10] 
print("현재리스트:",list) 
list.append(40) 
print("append(40)한 후의 리스트:",list)
a= list.pop(3) 
print("pop()으로 추출한 값:",a) 
print("pop()후의 리스트:",list)
list.sort()
print("sort()후의 리스트:",list) 
list.sort(reverse=True)
print("reverse()후의 리스트:",list ) 

''' 
QUIZ2: 리스트 초기값 [30,20,10] 설정 후 아래와 같이 출력되도록 코드작성
현재리스트: [30,20,10] 
10 값의 위치: 2 
insert(2,200) 후의 리스트: [30,20,200,10]
remove(200) 후의 리스트:[30,20,10] 
extend([555,666,555])후의 리스트:[30,20,10,555,666,555] 
555값의 개수: 2
''' 
list= [30,20,10]  
print("현재리스트: ",list) 
print("10값의 위치: ",list.index(10)) 
list.insert(2,200) 
print("insert(2,200)후의 리스트:",list) 
list.remove(200) 
print("remove(200)후의 리스트:",list) 
list.extend([555,666,555]) 
print("extend([555],[666],[555])후의 리스트:",list)  
print("555 값의 개수:",list.count(555))

#2차원 리스트
#리스트 안에 멤버 중 리스트가 존재하는 경우 사용되는 방식 
#리스트 안에 있는 멤버에 대한 참조방식  

#예제1] 2차 리스트 변수값 참조 
aa= [ [1,2,3,4], #aa[0]
     [5,6,7,8],  #aa[1]
     [9,10,11,12] ] #aa[2]
#aa리스트 멤버의 개수: 3 => [1,2,3,4], [5,6,7,8], [9,10,11,12] 
print(len(aa)) 
print(aa) 
for x in range(len(aa)): #aa리스트의 멤버수: 3 
    for y in range(len(aa[x])): #aa멤버 리스트의 멤버의 갯수:4 
        print(aa[x][y], end= '\t')
    print()  

# 예제 2] 2차 리스트 생성 및 출력
ls_1 = [] ; ls_2 = []; value = 1
# 2차 리스트 생성
for i in range(3):  # 상위 리스트의 멤버 갯수
    for j in range(4): # 하위 리스트(멤버)의 맴버 갯수
        ls_1.append(value)
        value += 1
        # 1st-ls_1 = [1,2,3,4],2nd-ls_1 = [5,6,7,8], 3rd-ls_1=[9,10,11,12]
    ls_2.append(ls_1)   # 1st-[[1,2,3,4]], 2nd-[[1,2,3,4],[5,6,7,8]], 
                        # 3rd-[[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    ls_1 = []
print(ls_2)   # [[1,2,3,4],[5,6,7,8],[9,10,11,12]]

# 출력(읽기)
for x in range(len(ls_2)):            # aa리스트의 맴버수 : 3
    for y in range(len(ls_2[x])):     # aa멤버 리스트의 멤버의 갯수 : 4
        print(ls_2[x][y], end='\t')
    print()


# 문제1] numbers= [10,20,30,40,50,60,70] 의 모든 값을 더한 결과를 출력하세요 
numbers= [10,20,30,40,50,60,70] 
print(sum(numbers))

# 문제2] 1-45까지 임의의 중복없이 6개 생성하여 출력 
from random import random, randint, randrange
lotto=[] 
cnt= 0 #출력개수 
while True: 
    rand= int(random()*45)+1 
    if rand not in lotto: 
        lotto.append(rand)
        cnt+=1
        if cnt==6: 
            break
lotto.sort() 
print(lotto)
    
# 문제3] 1st_sec= [['홍길동','남',36],['김수양','여',32],['박담수','남',28]] 
# 위 2차 리스트 자료를 다음과 같은 형식으로 출력 
# 이름: 홍길동 
# 성별: 남 
# 나이: 36
lst=[["홍길동","남",36],["김수양","여",32],["박담수","남",28]]
for i in range(len(lst)): 
    for j in range(1):
        print("이름:",lst[i][j])
        j+=1
        print("성별:",lst[i][j])
        j+=1
        print("나이:",lst[i][j])
    print() 
## or 
for val in lst: 
    print(f"이름:{val[0]}")
    print(f"성별:{val[1]}")
    print(f"나이:{val[2]}")
    
# 문제4] 구구단을 출력하는 코드를 작성하되, 2차 리스트에 결과값을 저장하고 출력할 수 있도록 하시오 
gugu=[ ]
for x in range (2,10): 
   gugu.append([]) #gugu에 비어있는 리스트 추가  
   for y in range(1,10): 
       gugu[x-2].append(x*y)
#여기까지 구구단의 결과값을 2차리스트로 만듬 

for x in range(2,10): 
    for y in range(1,10): 
        print( "{} x {} ={:<3}".format(x,y,gugu[x-2][y-1]),end="")
    print() 

#===========================
'''
list 내포(List Comprehension): 리스트 안에서 for와 if를 사용하는 문법 
형식1(for)
    변수 =[실행문 for 변수 in 열겨형객체]

    *for문의 실행 결과가 변수 리스트에 append되어 처리된다.  
'''
x= [2,4,1,5,7] 
lst=[ ] 
for i in x: 
    i**=2
    lst.append(i)
print(lst)

#또는 형식1 
lst1=[i**2 for i in x] # x 열거형자료(list)의 멤버들을 i**2로 append 한다. 
print(lst1)

#형식2(for와 if문 같이 사용) 
# 변수 = [실행문 for 변수 in 열거형객체 if 조건문] 
# 1~10 -> 2의 배수추출 -> i*2 -> list에 저장  
num= list(range(1,11)) #num리스트: [1,2,3,4,5,6,7,8,9,10] 
print(num) 
lst2= [i*2 for i in num if i%2==0] 
print(lst2)

'''
아래와 같은 메뉴를 만들고 친구 이름을 관리하는 코드를 작성 
(리스트 사용) 
-----------------
1. 친구리스트 출력     #등록한 친구보기
2. 친구추가          #친구 등록하기(정보는 문제3번 참조)
3. 친구삭제          #등록친구삭제
4. 이름변경          #이름변경  
5. 종료             #프로그램종료  
메뉴를 선택하세요: 2 
이름을 입력하세요: 홍길동 
------------------
'''
print("-"*10)
print("1.친구리스트 출력") 
print("2.친구추가")
print("3.친구삭제")
print("4.이름변경")
print("0.종료") 
menu= int(input("메뉴를 선택하세요:"))
friend=[] 
if menu ==1: #친구리스트출력 
   print(friend)
elif menu==2: #친구이름추가  
    name=str(input("이름을 입력하시오:")) 
    friend.extend(f"{name}") 
    print(friend)
elif menu==3: #친구삭제
    name=input("이름을 입력하시오:")
    friend.remove(f"{name}") 
    print(friend)
elif menu==4: #이름변경 
    name=input("이름을 입력하시오:")
    print("변경할친구이름: ",name) 
    delfriend= friend.index(name)
    print("변경전친구이름:",friend[delfriend])
    friend[delfriend]=name
    print(friend)
elif menu==5:
    print() 