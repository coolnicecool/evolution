import random
import threading
import time
import math
from playsound import playsound
#import RPi.GPIO as GPIO
import sys
import settings
settings =settings.settings
octatcat =""
#import Keypad       #import module Keypad
ROWS = 4        # number of rows of the Keypad
COLS = 4        #number of columns of the Keypad
keys =  [   '*','7','4','1',    #key code
            '0','8','5','2',
            '-','9','6','3',
            'D','c','B','i'     ]
rowsPins = [12,16,18,22]        #connect to the row pinouts of the keypad
colsPins = [19,15,13,11]
lessage =''        #connect to the column pinouts of the keypad
cat="cat"
turn=1
def sinput(message):
    global octatcat
    global lessage
    lessage =message
    if settings[0][1]=="keyboard":
       octatcat =input(message)  
    if settings[0][1]=="keypad":
       print(message)
       getkey()
def getkey():
    global octatcat
    codecat ="typing"
    blank =0
    o=""
    octatcat=""
    while codecat =="typing":
      keypad = Keypad.Keypad(keys,rowsPins,colsPins,ROWS,COLS)    #creat Keypad object
      keypad.setDebounceTime(5)      #set the debounce time
      key = keypad.getKey()       #obtain the state of keys
      if key =="D":
         codecat = 'done'
      if key =="B":
         octatcat =octatcat[:d]
         key =keypad.NULL  
         d=len(octatcat)
         d=d-1
         while blank <= 100:
             print(" ")
             blank = blank+1
         print(lessage)
         print(octatcat)
         blank=0
      if key != keypad.NULL and key !="D":
         while blank <= 100:
             print(" ")
             blank = blank+1
         print(lessage)
         blank=0
         o=key
         octatcat = octatcat+key
         d=len(octatcat)
         d=d-1
         print(octatcat)
         
foo=1
ledPin =11
#GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location
#GPIO.setup(ledPin, GPIO.OUT)   # Set ledPin's mode is output
#GPIO.output(ledPin, GPIO.HIGH)
m1=0.0
m2=0.0
m3=0.0
m4=0.0
p =1.0
ps=1.0
fruit =20
end =0
octatcat =""
#camo,strenght,speed,bag,fullness                                            
aa=[1.0,1.0,1.0,2.0,0,1]
ab=[1.0,1.0,1.0,2.0,0,1]
ac=[1.0,1.0,1.0,2.0,0,1]
ad=[1.0,1.0,1.0,2.0,0,1]
ae=[1.0,1.0,1.0,2.0,0,1]
A = [aa,ab,ac,ad,ae]
def mutate():
   global m1
   global m2
   global m3
   global m4
   m1=0.0
   m2=0.0
   m3=0.0
   m4=0.0
   d=0
   MR = random.randint(1,12)
   mutators = [m1,m2,m3]
   for i in range(3):        
        c = random.randint(1,12)
        if c==1:
          c = random.randint(0,64)
          if c in range(0,16):
            d = .2
          if c in range(17,32):
            d = .1
          if c in range(33,48):
            d= -.1
          if c in range(49,64):
           d= -.2
          mutators[i]=d
   m1=mutators[0]
   m2=mutators[1]
   m3=mutators[2]
   if MR==1:
        mr = random.randint(1,64)
        if mr in range(1,4):
           m4 = 1
        if mr in range(5,8):
           m4 = -1
        if mr in range(9,64):
           m4=0

def preator():
  global p
  global ps
  for c in [aa,ab,ac,ad,ae]:
    d= 3*c[2]
    d =round(d)
    q= random.randint(1,d)
    if q ==1:
      if p >c[1] and ps >c[2]:
          c[4]=0
          c[5]=0
      else:
          p=p+1
          ps=ps+1
def ssort(val):
    return val[2]
def gsort(c):
    return c[4]
def alive(c):
    return c[5]
def ort():
    global A

    A = list(filter(alive, A))
    A.sort(reverse=True, key=gsort)
    if octatcat =="2"or settings[1][1]=="on":  
      print('Total A:',A)
    A = A[0:5]
    if octatcat == "2"or settings[1][1]=="on":
      print('Filtered A:',A)
def food():
  global A
  global fruit
  global octatcat
  d = fruit
  A.sort(reverse=True,key=ssort)
  for c in A:
      if(c[3]<=0):
        c[4]=0
      else:
        ffruit=fruit
        fruit = max(fruit - c[3], 0)
        c[4]=ffruit-fruit
  fruit=d+1
  if octatcat =="2"or settings[1][1]=="on":    
    print("fruit:",fruit)
def gen():
  l=0
  f=0
  global m1
  global m2
  global m3
  global m4
  global A
  global ae
  global octatcat
  global turn
  f =len(A)
  for i in range(f):
   l=0
   g=0
   e = ae[4]/5
   e = math.floor(e)
   c= A[1-1][4]
   while l<A[i][4]:
      d =A[i][4]
      mutate()
      if m1+m2+m3+m4 !=0:
         if octatcat =="2"or settings[1][1]=="on":
            print("m1-4:",m1,m2,m3, m4)  
         A[i][0] = round(A[i][0]+ m1,1)
         A[i][1] = round(A[i][1]+ m2,1)
         A[i][2] = round(A[i][2]+ m3,1)
         A[i][3] = round(A[i][3]+ m4,1)
         if ae[4] >= 20 and A[i][4] >=d+e and A[i][4] >=c or ae[4] <20 and A[i][4] >=d:
            if g >=5 and A[i][4] != ae[4] or g <5:
               A.append(A[i][0:6].copy())
               g=g+1
               
      l=l+1
  ort()
  A =A[0:5]
  if turn <=10:
        b =len(A)
        while b != 5:
         b = len(A)
         c=b-1        
         if b<5:
           A.append(A[c])
  if octatcat =="2"or settings[1][1]=="on":    
    print(A)
def gall():
  global turn
  food()
  preator()
  gen()
  turn=turn+1
def lall():
    global end
    end =1    
def main(a,):
  global octatcat
  global settings
  global turn
  global A  
  global end
  landcat=[]
  A=a
  sinput("press 1 to stop press (i for info) anything else to go ")
  while octatcat != "1":
    if settings[1][1]=="on":
        f=1    
        while f==1:
            r =1  
            for i in settings:
              d=str(r)
              d=d+"."+i[0]
              print(d,i[1])
              r=r+1
        f=2  
    lop =1
    food()
    preator()
    gen()
    if octatcat =="*":
      w =len(settings[2])
      if w==1:
        settings[2].append(landcat)
      else:
        settings[2][1]=landcat  
      f=1    
      while f==1:
        r =1  
        for i in settings:
         if len(i)==3:
          d=str(r)
          d=d+"."+i[0]
          print(d,i[1])
          r=r+1
         if len(i)==2:
           print("not chanable")
           print(i[0],'=',i[1][0])
        sinput("enter the setting's number you want to change ")  
        octatcat=int(octatcat)
        r=octatcat-1
        sinput("press 1 to change "+ settings[r][0] +" to "+settings[r][2]+" ,2 to change it to the default setting, else nothing ")
        oc=octatcat
        sinput("to exit press 1 ")
        if octatcat=="1":
            f=0  
            octatcat ="*"
            if oc =="1" or oc =="2":
              d = settings[r][1]
             
              settings[r][1]=settings[r][2]
              settings[r][2]=d
              d=str(settings)
              g = "settings="+d
        if oc =="2":
             wrt = open("settings.py","w")
             wrt.write(g)
             wrt.close()  
    if octatcat =='0':
         loo=""           
         sinput('how may generations ')
         octatcat = int(octatcat)
         pro = (octatcat/(octatcat/(100*(4*(octatcat/100))))/100)
         pra =pro
         while lop!=octatcat:
            food()
            preator()
            gen()
            lop=lop+1
            turn =turn+1
            if lop == pro:
               pre = pro/(octatcat/100)
               loo=loo+"*"
               print("\r"+loo,end="")
               pro =pro+pra      
    if octatcat =="c":
         aa=[1,1,1,2,0,1]
         ab=[1,1,1,2,0,1]
         ac=[1,1,1,2,0,1]
         ad=[1,1,1,2,0,1]
         ae=[1,1,1,2,0,1]
         A=[aa,ab,ac,ad,ae]
         turn =0
    if octatcat =="i":
         print("press 2 for stat, 3 for 10 genration,4 for 100 etc till 8, press 9 for timed amount, 0 for what you choose, * for settings, and c for clear ")
         print("""111111 highest genoration    
       [663170.2, 666763.9, 848223.0, 55676.0, 55660.0, 1]
       [663158.2, 666752.0, 848187.2, 55660.0, 55660.0, 1]
       [663158.2, 666752.0, 848187.2, 55660.0, 55660.0, 1]
       [663158.2, 666752.0, 848187.2, 55660.0, 55660.0, 1]
       [663158.4, 666752.0, 848187.2, 55660.0, 55660.0, 1]""")
    if octatcat =="3":
         while lop !=10:
            food()
            preator()
            gen()
            lop =lop+1
            turn =turn+1
    if octatcat =="4":
         pro=25
         while lop !=100:
            food()
            preator()
            gen()
            lop =lop+1
            turn =turn+1
            if lop == pro:
              pre = pro/1
              print(pre,"% done")
              pro =pro+25
    if octatcat =="5":
        pro =50      
        while lop !=1000:
           food()
           preator()
           gen()
           lop =lop+1
           turn =turn+1
           if lop == pro:
              pre = pro/10
              print(pre,"% done")
              pro =pro+50
    if octatcat =="6":
        pro =100      
        while lop !=10000:
           food()
           preator()
           gen()
           lop =lop+1
           turn =turn+1
           if lop == pro:
              pre = pro/100
              print(pre,"% done")
              pro =pro+100                                
    if octatcat =="7":
        pro =500      
        while lop !=100000:
           food()
           preator()
           gen()
           lop =lop+1
           turn =turn+1
           if lop == pro:
              pre = pro/1000
              print(pre,"% done")
              pro =pro+500
    if octatcat =="8":
        d=2
        lee =0
        sinput("1 for time repeat, 2 for number(linenar) reapeat ")
        oc =octatcat
        sinput("number ")
        oca = int(octatcat)
        sinput("how many times do you want to do this (- for forever) ")
        ocat = octatcat
        if ocat[0] =="-":
           d =1
           ocat = ocat[1:]
        if ocat[0] =="+":
            lee =1
            ocat = ocat[1:]
        ocat = float(octatcat)    
        octatcat ="8"
        while ocat !=0 or ocat <0 or d==1:
            if lee ==1:
              aa=[1,1,1,2,0,1]
              ab=[1,1,1,2,0,1]
              ac=[1,1,1,2,0,1]
              ad=[1,1,1,2,0,1]
              ae=[1,1,1,2,0,1]
              A=[aa,ab,ac,ad,ae]
              turn =0
            end=0          
            if oc =="1":
              timer = threading.Timer(oca, lall)
              timer.start()
              while end !=1:
                gall()
            if oc =="2":
               oca = int(oca)
               print(oca)
               lop =0
               while lop!=oca:
                food()
                preator()
                gen()
                lop=lop+1
                turn =turn+1
            if d !=1:
              ocat = ocat-1
            e=0  
            print(turn)
            landcat.append(turn)
            while e<=4:
              print(a[e])
              e=e+1
        octatcat="8"
        e=len(landcat)
        r=0
        d=0
        while r <=e:
          q=r-1
          r=r+1
          print(q)
          d=d+landcat[q]
        d=d/r  
        d=round(d)
        landcat.insert(0,d)      
    if octatcat =="9":
        end=0
        sinput("type how many seconds ")
        octatcat = float(octatcat)
        timer = threading.Timer(octatcat, lall)
        timer.start()
        while end !=1:
          gall()
    print(turn)
    print("    ",A[0],"""
    """,A[1],"""
    """,A[2],"""
    """,A[3],"""
    """,A[4])
    turn = turn+1
    sinput("press 1 to stop press (i for info) anything else to go ")
  if octatcat ==1:    
    print("octacat")
    sys.exit()
if __name__ == "__main__":
   while foo==1:  
    try:
        main(A)
    except KeyboardInterrupt:
         foo=1