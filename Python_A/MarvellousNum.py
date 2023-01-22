def ChkPrime(a):
    prime=[]
    for i in a:
        c=0
        for j in range(1,i):
            if i%j==0:
                c=c+1
        if c==1:
            prime.append(i)
    print(prime)
    
    Add=Sum(prime)

    print("Sum of all prime numbers in the given list is : ",Add)
   
def Sum(b):
    s=0
    for i in b:
        s=s+i
    return s