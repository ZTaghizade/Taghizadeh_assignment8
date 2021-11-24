class complex:
    def __init__(self,a,b):
        self.re=int(a)
        self.im=int(b)
    def sum(num1,num2):
        real=num1.re+num2.re
        imag=num1.im+num2.im
        real=str(real)
        imag=str(imag)
        return(real+"+"+imag+"i")
    def sub(num1,num2):
        real=num1.re-num2.re
        imag=num1.im-num2.im
        real=str(real)
        imag=str(imag)
        return(real+"+"+imag+"i")
    def mul(num1,num2):
        real=(num1.re*num2.re)+(num1.im*num2.im*-1)
        imag=(num1.im*num2.re)+(num1.re*num2.im)
        real=str(real)
        imag=str(imag)
        return(real+"+"+imag+"i")
while(True):
    print("""Please enter the number of your sellection:
1. Sum
2. Sub
3. Mul
4.EXIT""")
    n=int(input())
    if(n>3):
        break
    
    Real=input("Enter the first number: \nReal: ")
    Imag=input("Imaginary: ")
    ob1=complex(Real,Imag)
    Real=input("Enter the second number: \nReal: ")
    Imag=input("Imaginary: ")
    ob2=complex(Real,Imag)
    if(n==1):
        print(complex.sum(ob1,ob2))
    elif(n==2):
        print(complex.sub(ob1,ob2))
    elif(n==3):
        print(complex.mul(ob1,ob2))