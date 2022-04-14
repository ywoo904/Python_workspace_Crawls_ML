n <- 30 
result <- 1
for (i in 1:(n-1)) { 
    result <- result *(365-i)/365 
} 
print(result)