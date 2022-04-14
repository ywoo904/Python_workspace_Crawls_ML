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

# 연속된 값의 숫자 벡터경우 단위 증가 시 사용되지 않는 경우   
numbers4 <- 1.5:6.4 # [1] 1.5 2.5 3.5 4.5 5.5
numbers4 # 마지막 6.5는 출력이 되지 않는다.  

# 논리값 벡터 
log_values= c(TRUE,FALSE,TRUE,FALSE) 
log_values 

# 벡터 길이 알아오기(요소 갯수 알아오기) 
length(numbers4) # 벡터의 요소갯수: 5  

# 벡터의 문자열이나 숫자열을 정렬하여 처리하는 함수: sort() 
fruits <- c("banana","apple","orange","mango","lemon") #abc 
numbers <- c(13,3,5,7,20,2) #1-100 

sort(fruits)
sort(numbers)
 
# 벡터함수의 사용-> 인덱스 참조1 : c() 
fruits <- c("banana","apple","orange","mango","lemon") 
# 선택참조 
fruits[c(1,3,5)] 

# 인덱스 참조2
fruits <- c("banana","apple","orange","mango","lemon")  
# 선택제거 (-인덱스로 제거하여 출력 )
fruits[-1]  
fruits[-3] 
fruits[c(-1,-3)]

# 벡터의 반복: rep() 
# 요소의 반복
repeat_each <- rep(c(1,2,3), each=3)  #요소의 반복 
repeat_each # [1] 1 1 1 2 2 2 3 3 3

# 백터의 반복
repeat_times <- rep(c(1,2,3), times=3 ) #벡터를 반복 
repeat_times # [1] 1 2 3 1 2 3 1 2 3

# 요소의 개별반복
repeat_ind <- rep(c(1,2,3),times=c(5,3,2) )
repeat_ind #  [1] 1 1 1 1 1 2 2 2 3 3 

# 순차적인 벡터생성 
# 1
number1 <- 1:10
number1

# 2 seq() 함수사용 : 인자(from=(시작), to=(끝), by=(간격)) 
numbers2 <- seq(from=0, to=100, by= 20 )
numbers2 # [1]   0  20  40  60  80 100 

for (i in seq(from=0, to=100, by= 20 )) { 
    print(i)
}

## List: list() 함수사용, list라는 목록형 자료를 사용 (파이썬의 리스트와 비슷) 
#  문자열 리스트: 
strlist <- list('사과','바나나','체리')
strlist 

# 숫자형 리스트 
numlist <- list(10,20,30,40) 
numlist 


tlist <- list('사과',c(10,20,30),'바나나', '체리') 
tlist[2]

#[[1]]
#[1] 10 20 30 

# 리스트내 값 참조 
strlist <- list('사과','바나나','체리')
"사과" %in% strlist # TRUE 

# 리스트내 값 추가ㅣ: append() 
strlist <- list('사과','바나나','체리') 
#strlist <- append(strlist, "메론", after= 2)
strlist <- append(strlist, "포도") # after 가 없다면? 마지막에 추가 
strlist

# 리스트값 제거: 
#strlist <- strlist[-1] 
#strlist 

# 리스트 범위로 값을 출력 
strlist[2:5] 
(strlist)[2:5] 

# 리스트 결합 
list1 <- list("a", "b", "c")
list2 <- list( 1,2,3)
list3 <- c(list1,list2)
print(list3) 

# Matrices(행렬)- matrix()를 사용, nrow,ncol 값으로 정렬지정  
## 행렬생성1
tmatrix <- matrix(c(1,2,3,4,5,6),nrow=3, ncol= 2)   
tmatrix  

## 행렬생성2 
t2matrix <- matrix(c("apple","banana","cherry","orange"),nrow=2,ncol=2) 
t2matrix

## 행렬에 대한 접근 "[]"를 이용하여 접근 
t2matrix[1,2] 
t2matrix[2,] 
t2matrix[,2 ] 
 
# 하나 이상의 행렬에 접근
t3matrix <- matrix(c("apple","banana","cherry","orange","grape","pineapple","pear","melon","fig"),nrow=3,ncol=3) 
t3matrix 
t3matrix[c(1,2),] 
t3matrix[-3,] 
t3matrix[ ,c(1,3)]
t3matrix[,-2]

# 행렬에 값을 추가(컬럼추가): cbind()
newmatrix <- cbind(t3matrix,c("strawberry","blueberry","raspberry")) 
newmatrix 

# 행렬에 값을 추가(로우추가): rbind() 
newmatrix <- rbind(t3matrix,c("strawberry","blueberry","raspberry")) 
newmatrix 

# 행렬값 제거: 음수 인덱스 표시  
r1matrix <- newmatrix[-c(1,2),-c(3,4)] 
r1matrix

# 행렬값 확인 
"apple" %in% r1matrix  #False 
"apple" %in% newmatrix #True

# 행렬에 row와 column 알아오기 : dim() 함수 
dim(t2matrix)  
dim(t3matrix) 
dim(tmatrix)
dim(newmatrix)

# 행렬의 길이 
lmatrix <- matrix(c("apple","bananana","cherry","orange"), nrow= 2, ncol= 2)
length(lmatrix) 
lmatrix

#행렬에 반복문을 사용하여 row 와 column 값으로 행렬을 붙여와 보세요 

t4matrix <- matrix(c("apple","bananana","cherry","orange"), nrow= 2, ncol= 2) 

for(rows in 1:nrow(t4matrix)) { 
    for(columns in 1:ncol(t4matrix)){ 
        print(t4matrix[rows,columns])
    }
    } 

#행렬 합치기 
Matrix1 <- matrix(c("apple","banana","cherry","grape"), nrow=2, ncol=2) 
Matrix2 <- matrix(c("orange","mango","pineapple","watermelon"), nrow=2 , ncol=2) 

#row 로 더하기 : rbind() 
matrix_combined <- rbind(Matrix1, Matrix2 )
matrix_combined

#column 로 더하기 : cbind() 
matrix_combined <- cbind(Matrix1, Matrix2 )
matrix_combined

## Arrays 배열 
tarray <- c(1:24) 
tarray  #  [1]  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24
class(tarray) # "integer" 

multiarray <- array(tarray, dim= c(4,3,3))
multiarray
# *dim(4,3,3): 4는 rows, 3dms columns, 3은 행렬의 갯수(생성할 행렬의) 
# dim(nrow, ncol, 생성갯수)

# Arrays 값 접근 
multiarray[2,2,2] #18  #Array[row, col, 메트릭 번호] 

# c() 함수를 이용한 접근 
t2array <- c(1:24) 

## 첫번째 행렬의 첫번째 row에 접근 
tmultiarray <- array(t2array, dim =c(4,3,2))
tmultiarray[,c(1),1]

## 존재여부 
3 %in% tmultiarray

## row와 column 확인 
dim(tmultiarray) 

## Array 길이 
length(tmultiarray) 

# 반복문 사용  
for (x in multiarray) {
    print(x)

 } 

 ## Data Frames (data.frame()) 
 # 데이터프레임은 데이터를 테이블 형태로 표현하는 자료형 입니다. 
 # 데이터프레임 안의 데이터 타입은 서로 달라도 됩니다. 
 
 # 첫번째 칼럼은 문자(character), 두번째는 numeric, 세번째는 logical 로 생성해봅니다. 
 Data_Frame <- data.frame( 
     Training = c("Strength","Stamina","Other"), 
     Pulse= c(100,150,120), 
     Duration= c(60,30,45)
 )

 Data_Frame

 # summary() : 데이터프레임 값을 요약해서 보여줍니다  
 summary(Data_Frame) # 데이터프레임의 값을 요약해서 출력

Data_Frame[1] 
Data_Frame['Training'] 
Data_Frame$Training 

# Row 추가: rbind() 
 Data_Frame <- data.frame( 
     Training = c("Strength","Stamina","Other"), 
     Pulse= c(100,150,120), 
     Duration= c(60,30,45)
 )

New_Row_DF <- rbind(Data_Frame,c("Speed",110,110))
New_Row_DF

## Column 추가: cbind() 
 Data_Frame <- data.frame( 
     Training = c("Strength","Stamina","Other"), 
     Pulse= c(100,150,120), 
     Duration= c(60,30,45)
 )

New_Col_DF <- cbind(Data_Frame,Steps=c(1000,6000,2000)) 
New_Col_DF

## row와 column 제거 
Data_Frame_New <- Data_Frame[-c(1),-c(1)] 
Data_Frame_New

## ncol(), nrow () 
ncol(Data_Frame) #3 
nrow(Data_Frame) #3

## 요소갯수(길이) 
length(Data_Frame) #3 Training, Pulse, Duration 으로 시리즈가 3개이다 

# 결합: rbind()  
 Data_Frame1 <- data.frame( 
     Training = c("Strength","Stamina","Other"), 
     Pulse= c(100,150,120), 
     Duration= c(60,30,45) )

 Data_Frame2 <- data.frame( 
     Training = c("Strength","Stamina","Other"), 
     Pulse= c(100,150,120), 
     Duration= c(60,30,45) )

 New_Data_Frame <- rbind(Data_Frame1, Data_Frame2)
 New_Data_Frame


# 결합: cbind()  
 Data_Frame3 <- data.frame( 
     Training = c("Strength","Stamina","Other"), 
     Pulse= c(100,150,120), 
     Duration= c(60,30,45) 
     )

 Data_Frame4 <- data.frame( 
     Steps= c(3000,6000,2000),
     Calories = c(300,400, 300)

 New_Data_Frame1 <- cbind(Data_Frame3, Data_Frame4)
 New_Data_Frame1

 ## Factors (factors()): 범주형 자료일때 사용 
 # :정해진 범위 내에서 카테고리별로 분석을 하기 위해서 사용되는 데이터 자료형 
 # 예) 성별: 남성/여성, 음악: 록, 팝, 클래식, 재즈, 운동: 스테미나, 근력 
 
 # factor 생성 
 music_genre <- factor(c('Jazz','Rock','Classic','Pop','Jazz','Rock','Jazz'), levels= c('Classic','Jazz','Pop','Rock','Opera')) 
 music_genre #Levels: Classic Jazz Pop Rock 중복된 목록은 중복제거해서 정리 
 levels(music_genre) #[1] "Classic" "Jazz"    "Pop"     "Rock"   
 length(music_genre) # [1] 7 

 # levels: levels() -> 카테고리로 출력 
 length(music_genre)
 
 # 요소접근 
 music_genre[3] #Classic / Levels: Classic Jazz Pop Rock 
 
 # 요소의 변경  
 music_genre[3] <- 'Pop' 
 music_genre[3] #[1] Pop / Levels: Classic Jazz Pop Rock 

 # 주의) factor는 정해진 범주 내에서 카테고리별로 분석을 위해서 사용하기 때문에 
 # 사전에 정의되어있지 않은 값으로 변경 시 에러가 발생함  
 music_genre[3] <- 'Opera' #유효하지 않은 팩터로 수정을 명령하여 에러발생 

 ## 순열과 조합 
 # 순열: 서로 다른 것들이 있는 경우 그 중에서 몇개를 뽑아서 줄을 세우는 경우의 수
 # 여기서 줄을 세운다는 표현은 순서를 고려하는 의미 
 # 먼저 실행결과에 따라 그 뒤가 영향을 받는 것  
 # nPr- n번중 순서를 따지고 r번실행 
 # nCr- n번중 순서를 따지지 않고 r번 실행 

# 팩토리얼 구하는 코드 
fact <- function(n) {  
    x <-1 
    for (i in 2:n) {
        x<-x*i 
    } 
    return (x)
}
fact(10) 
######################################
x <- c(1,2,3,4,5)
count <- 0
for (i in 1:5) { 
    x2 <- x[x !=i] # i 에 저장된 값 빼고 x2 저장 
    for (j in 1:4) { 
        print(c(i,x2[j])) 
        count <- count + 1 
    }
}

print(count) #20 # (1,2) (1,3) (1,4) (1,5) (2,1) (2,3) (2,4) (2,5)... 

# => 공식을 이용한 경우 nPr = n!/(n-r)! 
perm <- function(n,r) { 
    return(fact(n)/fact(n-r))
} 
perm(5,4) #60 

## 조합은 순서를 고려하지 않는다 (1,2),(2,1) 
# 순서를 고려하지 않기 때문에 같은 값이 있다면 이것은 하나의 값으로 처리됨

# nPr/r! = nCr, 이유는 순서의 쌍이 같은 값으로 구성되기 때문이다 
# (1,2,3), (1,3,2), (2,1,3),(2,3,1),(3,1,2),(3,2,1)

# 하지만 조합은 1개만 존재한다. 왜? 모두 1,2,3이 포함되어 있으니까...

## 조합을 계산하는 코드 
x <- c(1,2,3,4,5)
count <- 0
for (i in 1:4) { 
    for (j in (i+1):5){ 
        print(c(i,j)) 
        count <- count + 1 
} 
} 

print(count) # 10 

##nPr = n! /(n-r)! 
##nCr = nPr / r!  => n!/(n-r)!/r! 
comb <- function(n,r) { 
    return(fact(n)/fact(n-r)/fact(r)) 

} 
comb(45,6) #2.5



