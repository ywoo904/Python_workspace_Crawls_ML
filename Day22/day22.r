## 문자열
# 1. 문자열  
str <- "Hello R!!" 
print(str) 

# 2. 여러줄 문자열
str2 <- "Lorem ipsum dolor sit maet,
consec aselkrjasj r;kasejr lkas,
asekltjhaslektjaset , 
asekl" 

# 출력: [1] "안녕 친구야 \n오늘도 좋은 하루가 되길 바래. \n밖에 날씨는 어때" 

# 3. 동일하게 "\n" 표현되도록 출력하고 싶다면 cat() 
str2 
cat(str2)

# 4. 문자열길이(nchar(str))
nchar(str)
nchar(str2)

# 5. 문자열 내에 글자 확인 함수: grepl() 
str4 <- "Hello World"
grepl("H",str4) #TRUE 
grepl("Hi",str4) #FALSE 

# 6. 문자열의 결합: paste()
str5 <- "Hello"
str6 <- "R---" 
paste(str5,str6)

# Escape 문자 : \\(역슬러시를 문자열로 표현), \n, \r(문장앞으로 커서이동), \t, \b(백스페이스, 커서이동)

## 조건문: if
#if( ) { 
    #조건실행문 
#} 

#if( ) { 
    #조건실행문 
#} else{ 
    #조건실행문 
#}

#if( ) { 
    #조건실행문 
#} else if ( ){ 
    #조건실행문 
#} else{ 
#   } 

# **중첩 
# x가 10일 경우 if문을 사용하여 2의 배수이면 "2의 배수", 6배수이면 "6의 배수를 사용하게  "


intext <- readline("입력하세요:")
num <- as.numeric(intext)

if (num%%2 == 0) {
    print("2의 배수")
}

if (num%%6==0) {  
    print("6의 배수")
}

## 반복문: while, for
# next는 (continue), break는 반복문 종료 

i <- 0
while(TRUE) {  
    i <- i + 1  
    if (i==3) { 
        break
    }
    print(i)
} 

# for 문도 비슷하게 사용이 가능함 
dice= c(1,2,3,4,5,6) 

for (x in dice ) { 
    print(x)
} 

for (x in 1:6 ) { 
    print(x)
} 

x <- 1  
for (i in 2:10) { 
    x <- x*i 
    print(x)
} 

## 함수만들기(function 명령어), if 문의 구조와 비슷  
# 함수명 <- function(인자리스트) {  
# 함수정의부 
#}
# return() 함수 -> 실행 결과를 리턴 
# 함수호출: 함수명(인자)

## 팩토리얼 함수 만들기 
fact <-
function(n) { 
     x <- 1  
     for(i in 2:n) {
        x<- x*i 
    }
    return(x)
}

fact(10)

## 함수중첩예시
Nested_function <- function(x,y) {
    a <- x +y 
    return(a)

 }  

Nested_function(Nested_function(2,2),Nested_function(3,3)) 
# 2+2 / 3+3  => 4+6 

## 함수중첩예시2
Outer_func <- function(x) { 
    Inner_func <- function(y) { 
        a <- x+y 

        return (a)


    }
    return(Inner_func)
} 

output <- Outer_func(3)
output(17) # 8 

## 숫자를 입력받아 그 숫자를 역으로 출력한 프로그램을 함수로 만드세요 
reverse <- function(x) {
    result <- 0 
    while (TRUE) { 
        temp <- x %%10  #1234 => 4 
        x <- x %/% 10   #1234 => 123
        result <- (result + temp)*10

        if (x==0) { 
            break
        }
    }  
    return(result%/%10)
 }  

su <- readline("숫자를 입력하세요") 
num <- as.numeric(su)
reverse(num)



## 두 수를 입력받아 그 평균을 구하는 함수를 만드세요
avg_func  <- function() { 

    intext1 <- readline("Insert first number")
    num1 <- as.numeric(intext1)

    intext2 <- readline("Insert second number")
    num2 <- as.numeric(intext2) 

    tot <- num1 + num2
    avg <- tot / 2

    return(avg)
    
}

avg_func() 


##재귀함수(스스로를 참조하는 함수)
# 무한루프이기 때문에 반드시 중단점이 필요 
try_recursion <- function (k) {
    if(k>0){
        result <- k + try_recursion(k-1)
        print(result)
    } else { #k가 0보다 작으면 
        result <- 0
        return(result)
    }
 }  

try_recursion(5)

##문제.. 재귀함수를 사용하여 팩토리얼 계산함수를 생성하세요
# fact_r 명으로 작성합니다. 
fact_r <- function(k) {
       
       if( k>1 ){ 
             result <- k * fact_r(k-1) 
             print(result)
        } else { 
         result <- 1
         return(result)
     }
}

fact_r(5)


# 전역변수 설정하기 
# 일반변수설정 
# 함수내의 지역변수와 전역변수는 다른것이다.  
txt <- "awesome" 
my_func <- function( ) { 
    txt <- "fantastic" 
    paste("R is",txt)
 } 

my_func() 
print(txt)

# 전역변수 설정하기
my_func <- function () {  
    txt <<- "fantastic" 
    paste("R is", txt)

}
my_func() 
print(txt) 

# 벡터: 같은 자료형의 연속된 리스트(배열) 

# 문자백터 
fruits <- c("banana","apple","orange")
fruits

# 숫자백터 
fruits <- c(1,2,3,4,5) 
fruits[3] #3

# 연속된 숫자의 백터생성 
numbers <- 1:10 
numbers 
numbers[9]

# 연속된 값의 표현은 정수 단위로 증가합니다.  
numbers3 <- 1.5:6.5  # [1] 1.5 2.5 3.5 4.5 5.5 6.5
numbers3 # 숫자를 무엇으로 사용하던 값의 증분은 정수 1씩 

#
numbers4 <- 1.5:6.4 # [1] 1.5 2.5 3.5 4.5 5.5
numbers4 # 마지막 6.5는 출력이 되지 않는다.  


