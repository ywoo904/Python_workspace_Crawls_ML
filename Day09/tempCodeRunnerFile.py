try: 
    num= int(input("나이입력:")) 
    
    if num<0:
        raise Exception("예외사항")
    
except ValueError:
    print("양의정수만 입력하세요!") 
except Exception as e: 
    print(e,"0보다 작은 나이는 존재하지 않습니다.")
else: 
    print("입력값출력{}- 예외처리 안된경우 실행".format(num)) 
finally:
    print("프로그램을 종료합니다.")