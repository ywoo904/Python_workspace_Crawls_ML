
n_sim = 1000 # 시뮬레이션 횟수 
n <- 30 #한번 추출할 때 30명 추출해서 평균값 산정 
means= vector(length=n_sim)  

for(i in 1:n_sim) { 
    y <- vector(length=n) #길이가 n인 저장소를 만든다 
    for(j in 1:30) { 
        gender <- rbinom(1,1,0.5) #개인별로 1명씩 성별을 추출
        if(gender==0) {# 여성집단 
            y[j] <- rnorm(1,160,5) #여성집단에서 키를 추출  
        }else  { 
            y[j]<- rnorm(1,175,5) #남성집단에서 키를 추출  
        }
     }
     means[i] <- mean[y]
}

hist(means,xlab="mean_height",ylab="prob", main="Distribution of means",prob=T) 
