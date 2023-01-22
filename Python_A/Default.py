

def Area(Radius,PI=3.14):
    Result=PI*Radius*Radius
    return Result

def main():
    Rvalue=10.5
    PIvalue=3.14

    Ans=Area(Rvalue,PIvalue)                     #Ans =Area(10.5,3.14)    #positional arguments
    print("Area of circle is  : ",Ans)

    Ans=Area(PI=PIvalue,Radius=Rvalue)           #Ans= Area(10.5,3.14)    #keyword arguments
    print("Area of circle is  : ",Ans)

    Ans=Area(10.5)                                #Ans =Area(10.5)   # positonal arguments ans second is default argument
    print("Area of circle is  : ",Ans)


    Ans=Area(Radius=10.5)                         #Ans =Area(10.5)   # keyword  arguments and second is default argument
    print("Area of circle is  : ",Ans)
    
    Ans=Area(PI=7.10,Radius=10.5)                  #Ans =Area(7.10,10.5)   # keyword arguments
    print("Area of circle is  : ",Ans)

    

if __name__=="__main__":
    main()
