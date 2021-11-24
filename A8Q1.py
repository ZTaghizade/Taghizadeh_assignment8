class franction:
    def __init__(self,a,b,c,d):
        self.sa=int(a)
        self.mb=int(b)
        self.sc=int(c)
        self.md=int(d)
    def sum(self):
        if(self.mb==self.md):
            res=self.sa+self.sc
            res=str(res)
            mdst=str(self.md)
            return(res+"/"+mdst)
        else:
            sres=(self.sa*self.md)+(self.sc*self.mb)
            mres=self.mb*self.md
            sres=str(sres)
            mres=str(mres)
            return(sres+"/"+mres)
    def sub(self):
        if(self.mb==self.md):
            res=self.sa-self.sc
            res=str(res)
            mdst=str(self.md)
            return(res+"/"+mdst)
        else:
            sres=(self.sa*self.md)-(self.sc*self.mb)
            mres=self.mb*self.md
            sres=str(sres)
            mres=str(mres)
            return(sres+"/"+mres)
    def mul(self):
        sres=self.sa*self.sc
        mres=self.mb*self.md
        sres=str(sres)
        mres=str(mres)
        return(sres+"/"+mres)
    def div(self):
        sres=self.sa*self.md
        mres=self.mb*self.sc
        sres=str(sres)
        mres=str(mres)
        return(sres+"/"+mres)
    def sim(self):
        sres=self.sa
        mres=self.mb
        if(sres<mres):
            small=sres
        else:
            small=mres
        for i in range (small,1,-1):
            if(sres%i==0 and mres%i==0):
                sres=sres/i
                mres=mres/i
        sres=int(sres)
        mres=int(mres)
        sres=str(sres)
        mres=str(mres)
        return(sres+"/"+mres)
while(True):
    b=1
    d=1
    a=1
    c=1
    franc1=input("first franction: ").split("/")
    a=franc1[0]
    if(len(franc1)==2):
        b=int(franc1[1])
    
    print("""Enter the number of your sellection:
1.SUM
2.SUB
3.MUL
4.DIV
5.Sim
6.EXIT""")
    n=input()
    n=int(n)
    if(n!=5):
        franc2=input("Second franction: ").split("/")
        c=franc2[0]
        if(len(franc2)==2):
            d=int(franc2[1])
    ob=franction(a,b,c,d)
    if(n>5):
        break
    elif(b==0 or d==0):
        print("Denominator can't be '0'")
    elif(n==1):
        ans=franction.sum(ob)
        print(ans)
        array=ans.split("/")
        ob2=franction(array[0],array[1],1,1)
        print("Simplify: ",franction.sim(ob2))
    elif(n==2):
        ans=franction.sub(ob)
        print(ans)
        array=ans.split("/")
        ob2=franction(array[0],array[1],1,1)
        print("Simplify: ",franction.sim(ob2))
    elif(n==3):
        ans=franction.mul(ob)
        print(ans)
        array=ans.split("/")
        ob2=franction(array[0],array[1],1,1)
        print("Simplify: ",franction.sim(ob2))
    elif(n==4):
        ans=franction.div(ob)
        print(ans)
        array=ans.split("/")
        ob2=franction(array[0],array[1],1,1)
        print("Simplify: ",franction.sim(ob2))
    elif(n==5):
        print(franction.sim(ob))
    con=int(input("Do you want to try again? 1.YES 2.NO  "))
    if(con!=1):
        break