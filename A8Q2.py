class clock:
    def __init__(self,h,m,s):
        self.hour=h
        self.minute=m
        self.second=s
    def sum(fetime,setime):
        sec=min=hou=int(0)
        sec=fetime.second+setime.second
        if(sec>59):
            sec=sec-60
            min=min+1
        min+=fetime.minute + setime.minute
        if(min>59):
            min=min-60
            hou=hou+1
        hou+=fetime.hour + setime.hour
        sec=str(sec)
        min=str(min)
        hou=str(hou)
        return(hou+":"+min+":"+sec)
    def sub(fetime,setime):
        sec=min=hou=int(0)
        if(fetime.second<setime.second):
            sec=(fetime.second+60)-setime.second
            fetime.minute-=1
        else:
            sec=fetime.second-setime.second
        if(fetime.minute<setime.minute):
            min=(fetime.minute+60)-setime.minute
            fetime.hour-=1
        else:
            min=fetime.minute-setime.minute
        hou=fetime.hour-setime.hour
        sec=str(sec)
        min=str(min)
        hou=str(hou)
        return(hou+":"+min+":"+sec)
    def chstt(s):
        hou=int(s/3600)
        min=int((s%3600)/60)
        sec=int((s%3600)%60)
        sec=str(sec)
        min=str(min)
        hou=str(hou)
        return(hou+":"+min+":"+sec)
    def chtts(self):
        return((self.hour*3600)+(self.minute*60)+self.second)
while(True):
    print("""Please enter the number of your sellection:
1. Sum Time
2. Sub Time
3. Change second to time
4. Change time to second
5.EXIT""")
    n=int(input())
    if(n>4):
        break
    fhour=fmin=fsec=shour=smin=ssec=0
    if(n!=3):
        time1=input("Enter the first time: ").split(":")
        ob1=clock(int(time1[0]),int(time1[1]),int(time1[2]))
    if(n==1 or n==2):
        time2=input("Enter the first time: ").split(":")
        ob2=clock(int(time2[0]),int(time2[1]),int(time2[2]))
    if(n==1):
        print(clock.sum(ob1,ob2))
    elif(n==2):
        if(time2[0]>time1[0]):
            print(clock.sub(ob2,ob1))
        elif(time1[0]>time2[0]):
            print(clock.sub(ob1,ob2))
        elif(time2[1]>time1[1]):
            print(clock.sub(ob2,ob1))
        elif(time1[1]>time2[1]):
            print(clock.sub(ob1,ob2))
        elif(time2[2]>time1[2]):
            print(clock.sub(ob2,ob1))
        else:
            print(clock.sub(ob1,ob2))
    elif(n==3):
        se=int(input("Enter seconds: "))
        print(clock.chstt(se))
    elif(n==4):
        print("SECONDS: ",clock.chtts(ob1))