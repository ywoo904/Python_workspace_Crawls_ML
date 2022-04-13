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
# (1,2) (1,3) (1,4) (1,5) (2,1) (2,3) (2,4) (2,5)... 
print(count)

# => 공식을 이용한 경우 nPr = n!/(n-r)! 
perm <- function(n,r) { 
    return(fact(n)/fact(n-r))
} 
perm(5,4)