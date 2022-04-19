x <- subset(iris, Species=='virginica')$Petal.Length   
y <- subset(iris, Species=='versicolor')$Petal.Length

# 시뮬레이션 
n_sim <- 1000 

# 두 평균의 차이 
difs= c() 

# 시뮬레이션 작업 
for (i in 1:n_sim) { 
    # 표본추출
    bs_virginica <- sample(x,length(x),replace= T)
    bs_versicolor <- sample(y,length(y),replace= T)
    # 차이값(표본평균간) 
    mean_dif= mean(bs_virginica)- mean(bs_versicolor) 
    difs = c(difs, mean_dif) 
}

c(quantile(difs,.025),quantile(difs,.975))
# 1.09390 1.48005  


c(quantile(difs,.001),quantile(difs,.999))