def backwards(num): 
    list= [] 
    for i in range(len(str(num))): #i= 0,1,2,3 # 1234->4321 
       #3뽑기 1234%100= 34 34//10= 3
       #2뽑기 1234%1000= 234 234//100=2 
       #1뽑기 1234//1000
        if i ==0:
          list.append(num%10)
        elif i>0 and i < len(str(num))-1:
          list.append(num%10**(i+1)//10**i)
        elif i== len(str(num))-1: 
          list.append(num//10**i) 
    return list

txt=int(input("거꾸로 출력할 숫자를 입력하세요"))
result=backwards(txt) 
print(result)