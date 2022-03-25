def dic_func(**par): 
    print(par,type(par)) 
    for k in par: 
        print("{}:{}".format(k,par[k]))
#메인
dic_func(피카츄='1마리',파이리='2마리',꼬부기='없음',라이칸='1') 

dic= { 
      'sep': '-',
      'end': '\n\ntest'
} 
lst=['test1','test2','test3','test4'] 

print('test','test','test',**dic)
print('test','test','test',sep='-',end='\n\ntest')
print(*lst,**dic)