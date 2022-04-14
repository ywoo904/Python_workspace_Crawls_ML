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

