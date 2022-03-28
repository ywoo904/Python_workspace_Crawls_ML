def Adder(n): 
    if n==1: #종료조건 
        return 1 
    else:
        result = n+Adder(n-1) #재귀호출
        print(n, end= '') # 스택영역: 만약 n=5(시작) -> 2 3 4 5 
        return result 
#함수호출
print("n=1:", Adder(1))
print("\nn=5", Adder(5))