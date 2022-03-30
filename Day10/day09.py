#객체지향 프로그래밍
#1.클래스와 오브젝트(객체) 
# 클래스란? - 특정 대상을 지정하여 정의를 담고 있는 것 
#   -실세계의 것을 모델링하여 속성(Attribute,멤버변수)와 동작(Method)를 갖는 데이터 타입 
#   -python에서 string, int, list, dict... 모두 다 클래스로 존재  
#   -예로 학생이라는 클래스를 생성한다면, 학생을 나타내는 속성과 학생이 행하는 행동을 함께 정의가능
#   -즉 다루고자 하는 데이터와 데이터의 연산을 하나로 캡슐화하여 클래스로 표현가능  
#   -모델링에서 중요시하는 속성에 따라서 클래스의 속성과 행동이 달라짐 
 
# 객체(Object)-클래스에 정의된 대로 개별적으로 구성되어 있는 개별, 독립적인 대상의미  
a= [1,2,3,4,5] # list-> class 
print(help(a)) # Help on list object: ....
a.append('a') 
print(a)

#객체(Object)-클래스에 정의된대로 개별적으로 구성되어 있는 개별, 독립적인 대상의미 
# - 클래스로 생성되어 구체화된 내용(객체-인스터스) 
# - 파이썬은 모든것(int,float,str,list,dict,... etc)은 객체(인스턴스) 
# - 실제로 class가 인스턴스화되어 메모리에 상주하고 있는 상태를 의미  
# - class가 빵틀(설계도)등이라면, object(객체)는 실제로 빵틀에 찍어낸 빵을 의미함

##클래스 선언 
#객체를 생성하기 위해서는 객체의 모체가 되는 클래스를 미리 선언해야 한다. 
# (형식)
# class [클래스명]: 
#       변수선언(멤버변수-속성)
#       def 생성자(인수): 
#           명령문...
#       def 함수명(인수): 
#           명령문...
# 예제) 클래스 선언 
class Person:   
    pass #클래스 정의 나중에 만들기 위해서 pass를 사용 

# 객체생성  
bob= Person()
cathy= Person()

a=list() #빈 리스트 객체생성(Class)
b=list() 

print(type(bob),id(bob))
print(type(cathy),id(cathy))
print(type(a),type(b))

##클래스생성자
# -생성자, 클래스 인스턴스가 생성될때 호출됨 
# -__init__(self)가 기본으로 생성하게 된다. self가 인자로 오고 이는 자신을 가리킴
# 이름이 꼭 self일 필요는 없지만 관례적으로 self로 사용
# 생성자는 해당 클래스에서 다루는 데이터를 정의할 수 있음 
# 정의하는 데이터를 멤버변수, 속성이라고 부름  

class Person: 
    def __init__(self): #기본생성자 
        print(self,'is generated')
        self.name='홍길동' #이름속성  
        self.age= 18 #나이속성 

p1= Person() 
p2= Person() 

print(p1,p2) #생성자에 의해 생성 

p1.name='홍길자' 
p1.age=24 

print(p1.name, p2.name) 
print(p1.age,p2.age)

#생성자에게 인자값을 전달하여 속성값을 부여하고 싶은 경우
class Person: 
    def __init__(self, name, age=10): #기본생성자 
        print(self,'is generated')
        self.name= name #이름속성  
        self.age= age #나이속성 
p1= Person('bob',30)
p2= Person('Kate',20) 
p3= Person('홍길동')
print(p1.name,p1.age )
print(p2.name,p2.age )
print(p3.name,p3.age )

# 문제1] Calc_class라는 클래스를 선언 
# 속성값은 x,y로 두개를 초기화 구현 
# 생성자에서 x,y의 속성값은 받을 수 있게 생성 
# 객체를 생성하여 해당값을 참조해서 확인해보세요 

#메소드 정의 
# 멤버함수라고도 부름. 해당 클래스의 object에서만 호출가능 
# 메서드는 객체 레벨에서 호출되며, 해당 객체의 속성에 대한 연산을 행함 
# 호출은 객체.메서드()형태로 호출됨 
class Calc_class:
    #클래스변수: 속성 
    x=y=0
    def __init__(self,x,y):
       
        self.x= x
        self.y=y 
    #클래스의 매서드(함수) 
    def plus(self): 
        p= self.x+self.y
        return p
    def minus(self):
        m= self.x-self.y
        return m 
    
c= Calc_class(10,20) 
print(c.x,c.y) #10,20
print(c.plus()) #30
print(c.minus()) #-10

#[예제1] 자동차클래스 
class Car:
    
    #맴버변수 
    cc=0  #자동차cc 
    door=0 #문짝개수 
    calType= None #null
    
    #생성자 
    def __init__(self,cc,door,carType):
        #멤버변수 초기화  
        self.cc= cc
        self.door=door
        self.carType= carType #승용차, SUV, 경차  
        
    def display(self):
        print("자동차는 %d cc이고, 문짝인 %d개, 타입은 %s"
            %(self.cc,self.door,self.carType)) 

##객체생성
car1= Car(2000,4,"승용차") #객체생성 + 초기값 설정 
car2= Car(3000,5, "SUV")

car1.display()  
car2.display() 

#소멸자(Destructor): 생성자 반대 역할하는 소멸자는 __del__()이란 이름으로 제공 
#객체 사용이 완료되었을때 자동으로 실행. 객체를 메모리에서 소멸시키는 역할을 한다. 
# class multiply: 
#       # 생성자 
#        def __init__(self): 
#           self.x=x 
#           self.y=y 
#       # 소멸자 
#        def __del__(self): 
#               del.self.x  
#               del.self.y

## self  
# 파이썬에서 Method는 항상 첫번째 인자로 self를 전달 
# self는 현재 해당 매서드가 호출되는 객체 자신을 가리킴  
# C++/C#, Java 에서는 이를 this에 해당
# 이름 꼭 self일 필요는 없지만 관행적으로 self 사용함

# [예시] 
class Person: 
    name = None 
    age= 0 
    
    # 생성자
    def __init__(self,name,age): 
        print("self: ",self)  
        self.name=name
        self.age= age 
        
    def sleep(self): 
        print(self.name,"은 잠을 잡니다.")

a= Person('Abram',100)  
b= Person('홍길동',18)

print(a)
a.sleep() 
b.sleep()
b.age= 110 
print(b.age)
print(a.age)

# Method 타입 
# -instance method: 객체로 호출 
#   매서드는 객체 레벨로 호출되기 때문에, 해당 메서드는 호출한 객체에만 영향을 미침 
#   (위 예시의 경우에서 a_abram,b_홍길동 객체에만 따로 저장된다.)
# -class method: class로 호출 
#   클래스 메서드의 경우, 클래스 레벨로 호출되기 떄문에 클래스 멤버 변수만 변경가능  

class DatePro: 
    #멤버변수 
    content="날짜처리 클래스"
    
    #생성자 
    def __init__(self,year,month,day): 
        self.year=year
        self.month=month 
        self.day=day
        
    #객체메서드(instance method)
    def display(): 
        print("%d-%d-%d" %(self.year,self.month,self.day))
        
    #클래스메서드(class method) 
    @classmethod    #함수 잠식자 
    def date_string(cls,dateStr): #dateStr의 데이터는 '20220330' 
        #클래스멤버 
        year = dateStr[0:4]
        month=dateStr[4:6] 
        day= dateStr[6:]
        print(f"{year}년 {month}월 {day}일" )
        
#객체멤버호출
date=DatePro(2022,3,30) #생성자 
print(date.content) #날짜처리클래스
print(date.year) 
print(date.display)

#클래스멤버
print(DatePro.content) #날짜 처리 클래스 
#print(DatePro.year) #AttributeError 왜? 생성자에 의해서 생성되는 멤버변수 
DataPro.date_string('20230330')

#예제 
class Math: 
    
    @staticmethod
    def add(a,b): 
        return a+b
    
    @staticmethod 
    def multiply(a,b):
        return a*b 
    
print(Math.add(10,20))
print(Math.multiply(10,20))

#특수한 메서드
# __로 시작하고 __로 끝나는 함수들은 특수함수 
# 해당 매서드를 구현하면 커스텀 객체에 여러가지 파이썬 내장함수나 연산자를 적용가능 
# 오버라이딩 가능한 함수 목록은  
# https://doc/python.org/ko/3/reference/datamodel.html 에서 확인가능

#[예시] Point클래스 - 2차원 좌표평면 각 점(x,y)
# 연산 -> 두 점의 덧셈, 빨셈(1,2) + (3,4) =(4,6)
#       한점과 숫자의 곱셈(1,2)*3= (3,6)

class Point: 
    #생성자 
    def __init__(self,x,y): 
        self.x = x 
        self.y= y
    
    #특수 메서드 호출 add 
    def __add__(self,pt): 
        new_x= self.x+pt.x 
        new_y= self.y+pt.y
        return Point(new_x,new_y)
    
    def __str__(self):
        return f"({self.x},{self.y})"  
    
    
p1= Point(3,4) #p1 객체생성  
p2= Point(2,7)

p3= p1 + p2  # __add__ 
print(p1) #__str__
print(p2) 
print(p3)

##캡슐화: 자료와 알고리즘이 구현된 함수를 하나로 묶고 공용 인터페이스 만으로 
# 접근을 제한하여 객체의 세부 내용을 외부로부터 감추는 기법을 말함  

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

##클래스 상속(inheritance)
# 기존에 정의해둔 클래스의 기능을 그대로 물려받는 설정 
# 기존 클래스에 기능 일부를 추가하거나, 변경하여 새로운 클래스를 정의 
# 코드의 재사용
# 상속 받고자 하는 대상인 기존 클래스는 Parent, Super, Base 클래스라고 한다. 
# 상속 받는 새로운 클래스 Child, Sub, Derived 클래스라고 한다.a