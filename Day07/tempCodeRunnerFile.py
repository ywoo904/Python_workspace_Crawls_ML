
def calc(num1,num2,giho): 
    '''함수설명: 숫자2개, 사칙연산을 받아 계산하는 함수프로그램''' 
    if '+' in giho: 
        return num1+num2 
    elif '-' in giho: 
        return num1-num2 
    elif '*' in giho: 
        return num1*num2 
    elif '/' in giho: 
        return num1/num2 
    else: 
        return 0 

#메인 
import os

while True:
    os.system('cls')
    txt= input("수식을 입력하세요 ex)5+5 >>>")
    if '+' in txt:
        num1,num2=txt.split('+')
        num1= int(num1); num2= int(num1); giho='+';
    elif '-' in txt:
        num1,num2=txt.split('-')
        num1= int(num1); num2= int(num1); giho='-';
        
    elif '*' in txt:
        num1,num2=txt.split('*')
        num1= int(num1); num2= int(num1); giho='*';
        
    elif '/' in txt:
        num1,num2=txt.split('/')
        num1= int(num1); num2= int(num1); giho='/';
    else: 
        print("수익입력이 잘못됬습니다. \n 내용을 다시 확인해주세요.")
        os.system('pause')
        continue
    
    result= calc(num1,num2,giho) #함수호출
    if result !=0: #0인 경우 수식오류 
        if type(result) is not float: 
            print("계산결과는:",result)
        else: 
            print("계산결과는: {:.2f}".format(result))
    sel= input("계속 하시겠습니까?(Y/N):") 
    if sel== 'n':
        break
print ("프로그램 종료")