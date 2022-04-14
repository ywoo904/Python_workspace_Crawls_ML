n_simulation <- 3000
n_success <- 0 
for (i in 1:n_simulation) { 
    x <- sample(1:5,3,replace=F)
    if( x[1]>=4 ) n_success <- n_success + 1
    if(( x[1]==3 )&(x[2]>=2)) n_success <- n_success + 1 
    
 } 

 print(n_success) # 535
 stc <- n_success/n_simulation 
 print(stc)