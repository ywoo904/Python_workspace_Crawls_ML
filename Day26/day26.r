## 통계적 가설검증
# 과학자들이 매일 통계적 가설 검증을 활용합니다. 예로 새로운 코로나 19 백신이 개발되어 백신의 효과를 알고 싶다면, 이를 입증하기 위하여 
# 백신을 접종한 사람과 그렇지 않은 사람들을 비교했을 때 전자가 유의미하게 병에 걸릴 확률이 낮아야한다. 
# 이때에 사용하는 통계적 가설검증입니다.
# 두 집단에서 발병자료를 수집하고, 질병발생률에 차이가 없다고 가정했을 때 (백신의 효과 x) 일반적으로 관측될만한 자료인지 아닌지 확인한다. 
# 만약 수집된 자료가 백신효과가 없다는 가정하에 관측되기 매우 힘든 결과라면, 즉 백신을 맞은 통제군이 그렇지 않은 집단에 비해서 
# 질병발생률이 훨씬 낮다면 원래 가정인 "백신이 효과가 없다" 라는 주장을 기각하고 효과가 있다는 결론을 내립니다.  
# 쉽게말해, "안되는걸 찾는다". H0: u = 00 / H1: u > < =| 00  
# 그렇지 않고 자료가 두 집단 사이 차이가 없다고 가정해도 충분히 그럴 듯 하다면 백신이 없다는 주장을 기각하지 못한다. 

## 통계적 가설 검증에서는 "효과가 있다", "차이가 있다"를 검증하는게 아니라, 그런 효과나 차이가 없다는 주장을 반박하는 방식으로 
# 과학적 주장을 간접적으로 입증하는 방식으로 취약합니다. "~~~없다"  
# H0: u = xxx (Null Hypothesis, 귀무, 영가설) 
# H1: u < > =| (Alternative Hypothesis, 대립가설) 
# Null hypothesis를 기각하기 위한 일반적 도구는 p값(P-value)이지만 생략한다.  
# 대신 지금까지 살펴본 신뢰구간을 바탕으로 이야기한다. 가설검증에는 p값을 사용하든 신뢰구간을 사용하든 똑같은 결과가 나온다는 것을 
# 수학적으로 증명할 수 있지만 하지 않는다. 신뢰도 95%, 99%를 벗어났다 -> 차이가 없다. 

# 앞에서 iris 자료를 통해서 setosa 종의 Petal.Length의 모평균에 대한 추정치가 95% 신뢰도에서 [1.41, 1.51] 이라는 것을 확인했습니다. 
# 그런데 뒤집어 생각하면 이 신뢰구간을 이 구간 밖에 있는 값을 별로 그럴듯하지 않다는 이야기라는 것이다. 
# 즉, Petal.Length이 평균 1.3이라는 주장은 이 신뢰구간에 비추어 생각할 떄 별로 그럴듯한 가설은 아니다. 
# 모평균이 1.3이라는 주장은 기각할 수 있다(영가설) 

# 여기서 알 수 있는 것은 신뢰구간의 성질을 알 수 있다. 모평균 1.3은 신뢰구간 95% 확률 영역안에 없다. 
# 만약 모평균이 1.3인 상황에서 만들어졌다면 95% 신뢰구간안에 1.3이 포함되어 있었겠지만 그러지 않았다는 점이다. 
# 달리 생각하면 95%에 값이 옳은데도 불구하고 5% 확률로 기각이 될 수도 있음을 의미한다. 

# Type 1 Error: Null hypothesis 가 옳으나 우연성으로 Null hypothesis가 reject될 때. 
# 가설검증에서 사용되는 신뢰구간의 신뢰도를 100%에서 뺀 것과 같습니다.  

## 부트스트랩 신뢰구간을 활용한 가설검증 
# 앞에 iris 데이터 셋을 이용, versicolor 종과 virginica 종의 Petal.Length 모평균
# 사이에 차이가 있는지 검증해봅니다. 이를 입증하기 위해서 실제로 관측된 두 종의 Petal.Length 자료가
# Null hypothesis 하에 그럴듯 한지 판단해야한다. 만약 답이 "그렇지 않다"면 Reject the H0 and 
# make statement that "u is different from xx" 

# 프로그래밍 구현에서 두 종의 Petal.Length의 모평균이 같다면 두 종에서 각각 표본을 뽑아
# 계산한 표본평균들의 간의 차이도 대체로 0에 가까울 것. 
# 그리고 이를 반복적으로 시행해 모평균의 차이에 대한 신뢰구간을 어떻게든 만들면 
# 대부분의 신뢰구간은 0을 포함할것. 
# 문제는 모평균의 차이에 대한 신뢰구간을 만드는 방법이나 수학공식에 대해서 전혀 이야기되지 않고 있음 
# -> Bootstrap을 이용해 극복 

# 두 종의 자료수집(원래 표본과 같은 크기의 표본을 복원추출하고, 표본평균을 각각 계산한뒤 그 차이를 모음) 
# 그리고 신뢰구간을 작성하고 0이 그 구간에 포함되는지 확인하면 된다. 
# 포함되면 Do not Reject Ho, 포함되지 않으면 Reject Ho 
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

# 모평균의 차이에 대한 95% 부트스트랩 신뢰구간은 대략 [1.09390 1.48005] 
c(quantile(difs,.025),quantile(difs,.975))

# 모평균의 차이에 대한 99% 부트스트랩 신뢰구간은 대략 [1.007962 1.610000]
c(quantile(difs,.001),quantile(difs,.999))

# 두 신뢰구간 모두 0을 포함하지 않기 때문에 두 종의 Petal.Length의 모평균이 같다는 
# Null Hypothesis 는 95% 신뢰수준에서 기각할 수 있다. 

## 예측정확도의 역설 

