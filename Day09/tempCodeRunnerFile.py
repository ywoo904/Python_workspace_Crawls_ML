
import datetime,time
t= time.localtime()  
s= time.localtime().tm_zone  
print(t) #time.struct_time(tm_year=2022, tm_mon=3, tm_mday=28, tm_hour=21, tm_min=46, tm_sec=59, tm_wday=0, tm_yday=87, tm_isdst=1)
print(s) #EDT 
print(t.tm_year) #2022
print(t.tm_mday) #28 

start = time.time()  
print(start) #1970.01.01.00시를 기점으로 'How many seconds?' 
time.sleep(5)
end = time.time() 
print(end)