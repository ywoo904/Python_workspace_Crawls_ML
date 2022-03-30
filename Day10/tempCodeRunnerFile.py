
#예제3. 캡슐화  
class Account:
    #은닉변수
    __balance= 0 #잔액
    __accName= None #예금주 
    __accNo= None #계좌번호
    
    #생성자:멤버변수 초기화
    def __init__(self,bal,name,no): 
        self.__balance= bal #잔액
        self.__accName= name #예금주
        self.__accNo= no #계좌번호 
    
    #Getter (계좌정보 확인)
    def getBalance(self):
        return self.__balance, self.__accName, self.__accNo 
    
    #Setter (입금하기)
    def deposit(self, money): 
        if money <0:
            print("금액확인")
            return          #종료(exit)
        self.__balance +=money 
        
    def withdraw(self,money):   
        if self.__balance < money:
            print("잔액확인") 
            return      #종료(exit) 
        self.__balance -= money 
        
##객체생성(생성자로 초기값 설정)
acc= Account(10000,'홍길동','123-123-3333-13') 

##Getter: 예금확인
print("계좌정보:",acc.getBalance()) 

##Setter: 입금하기 
acc.deposit(50000) #50000원 입금
print("계좌정보:",acc.getBalance())

acc.withdraw(10000)
print("계좌정보:",acc.getBalance())