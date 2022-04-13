t <- 10 
t

# R 사용문법
# 실행은 Ctrl + Option + N  
# 변수사용하기 (대입연산은 "=" 대신 " <-" or or "->") 
# - 하나의 값을 변수에 저장하기  
x <- 5 
x*x
10 -> y 
y+y

# 2. 여러개의 값을 변수에 저장 (배열과 같은 자료 사용하기) 
x <- c(5,6) # 벡터변수, 여러개의 값을 하나의 변수에 저장 
print(x)

# 여러개의 가진 변수에 일부 값을 참조 시 인덱스를 사용
# R의 인덱스의 시작값은 1부터...
x[1] 
x[2] 

# 변수이름규칙
# -변수이름은 영문, 숫자, "." , "_" 를 사용 
# -하지만 .을 앞에 사용할 수 있음. 이때 뒤에 숫자는 안됨
# -변수 앞에 숫자나 _를 사용하면 안됨
# -변수명은 대소문자 구분 
# -예약어를 사용할 수 없음 


## 데이터 타입 
# numeric: 숫자(10.5,55,768)
# integer: integer 타입(숫자 L을 붙여서 표현)(1L,55L,100L) 
# complex: 복소수형(i를 붙여서 구분)
# character: 문자/문자열 자료
# logical: 논리형자료(TRUE/FALSE)

# 타입확인 함수: class() 
#class(10L) #integer 
#class(10) #numeric 
#class("th") #chracter
#class('test') #character 
#class(TRUE) #logical 

# r

a/b 
a^b 
a%%b
a%/%b  

## <-, <<-, ->, ->> 
# "<<-" 전역선언, <- 대입처리 

## 비교연산자  
# ==,!=, >, <, >=, <= 

## 논리연산자
# &,&&,|,||,! 

10==10 && 10==10 
!(10==10)

##이외 연산자 
# : 순서대로 순자를 생성하는 연산자 ex) 1:10 -> X 
# x는 (1,2,3,4,5,6,7,8,9,10)
# %in%: 데이터들(백터) 내에 값이 있는지 확인 
# %*%: 메트릭 곱하게 

1:10 -> x 
x <-5
i %in% x

# **print(), paste 
print(x) 
paste(x,i)
print('I','am','a','student')

# **print(), paste 
print(x) 
paste(x,i)
print("I","am","a","student") # error  
print('I','am','a','student')

# 내장함수 
# max(), min(), sqrt ()- 루트연산 abs() 절대값 ㄷ 
# ceiling()- 올림, floor()-내림 ->ceiling(1.4), floor(1.4)

max(c(11,5,36,3,4,8,33)) 
min(c(11,5,36,3,4,8,33)) 
sqrt(2)
abs(-100)
ceiling(1.4) 
floor(1.4)
round(1.456,2) 
