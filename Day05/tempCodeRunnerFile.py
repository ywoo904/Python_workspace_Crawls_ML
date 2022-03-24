print("-"*10)
print("1.친구리스트 출력") 
print("2.친구추가")
print("3.친구삭제")
print("4.이름변경")
print("0.종료") 
menu= int(input("메뉴를 선택하세요:"))
friend=[] 
if menu ==1: #친구리스트출력 
   print(friend)
elif menu==2: #친구이름추가  
    name=str(input("이름을 입력하시오:")) 
    friend.extend(f"{name}") 
    print(friend)
elif menu==3: #친구삭제
    name=input("이름을 입력하시오:")
    friend.remove(f"{name}") 
    print(friend)
elif menu==4: #이름변경 
    name=input("이름을 입력하시오:")
    print("변경할친구이름: ",name) 
    delfriend= friend.index(name)
    print("변경전친구이름:",friend[delfriend])
    friend[delfriend]=name
    print(friend)
elif menu==5:
    print() 