
y <- subset(iris, Species=='setosa')$Petal.Length  
n_sim <- 10000 
sds <- c()
n <- length(y) # 50개 

for (i in 1:n_sim) {  
    bs_sample = sample(y,length(y),replace=T) 
    sample_sd = sd(bs_sample)
    sds = c(sds,sample_sd)
}
c(quantile(sds,.025),quantile(sds,.975)) # 0.1300549 0.2101117 
(quantile(sds,.025)+quantile(sds,.975))/2

##구간추정공식(수학적공식)- 모 표준편차에 대한 구간추정 공식을 생략 
sqrt(var(y)*(n-1)/qchisq(.975,n-1))
sqrt(var(y)*(n-1)/qchisq(.025,n-1))

# 공식에 의한 값은 실제로 부트스트랩을 사용한 경우와 비교했을 때에 큰 차이가 나지 않는다. 
# 이는 각종 수학적 과정과 표본크기 등의 문제 때문에 복잡하니 생략  
# 중요한 것은 구간 추정법을 모르는 대상도 점추정법만 알면 복원 추출을 통해 구간추정을 할 수 있다 ->Boststrp을 이용하는 이유 

