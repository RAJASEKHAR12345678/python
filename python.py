def check_is_prime(m, n):
    
    
    r = ""
    
    for i in range(m,n+1):
        if i<0:
            r+=str(i)+" "
        else:
            c = 0
            for j in range(1,i+1):
                if(i%j ==0):
                    c+=1 
            if c ==2:
                r+=(str(i)+" ")
    return r           
                
           
    
m = int(input())
n = int(input())

prime_numbers = check_is_prime(m,n)
print(prime_numbers)