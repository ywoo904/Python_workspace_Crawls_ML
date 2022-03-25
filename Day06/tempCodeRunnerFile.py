# 1. 입력자료생성: 
import random 
dataset= [] 
for i in range(10): 
    r= random.randint(1,100) 
    dataset.append(r)
print(dataset)

# 변수초기화 
vmax= vmin= dataset[0]

# 최대최소값 구하기 
for i in dataset:
    if vmax < i: 
        vmax= i
    if vmin > i: 
        vmin=i 

#결과출력: 
print("max=",vmax,"min=",vmin)