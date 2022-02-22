from tkinter import *
import time
main=Tk()
main.title("F.L.A.M.E.S")
main.config(bg="Pink2")
main.geometry("420x240")
title=Label(text="Flames",bg="Pink2",font=("Aleo",35),fg="Red2")
title.place(x=125,y=20)
your=Label(text="Enter Your Name ",font=("Aleo",13),fg="Red2",bg="Pink2")
your.place(x=15,y=90)
patner=Label(text="Enter Your Patner's Name ",font=("Aleo",13),fg="Red2",bg="Pink2")
patner.place(x=200,y=90)
def opf():
 global patner_name,your_name
 if len(patner_name.get())>0 and len(your_name.get())>0:
  truth=Tk()
  truth.geometry("350x150")
  truth.title("The Moment Of Truth")
  truth.config(bg="Pink2")
  l1=Label(truth,text="",bg="Pink2",fg="Red2",font=("Aleo",15))
  l1.place(x=20,y=20)
  msg=Label(truth,text="",bg="Pink2",fg="Red2",font=("Aleo",10),wraplength=330)
  msg.place(x=20,y=60)
  def clt():
   truth.destroy()
  close2=Button(truth,text="Close",fg="Red2",bg="Pink2",command=clt)
  close2.place(x=295,y=120)
  x=list((your_name.get()).lower())
  y=list((patner_name.get()).lower())
  s=""
  c=0
  while c<len(x)-1:
   g=x[c]
   if g in y:
    x.pop(c)
    y.remove(g)
    c-=1
   c+=1
   print(g)
   print(x,y)
  f=x[0:len(x)]
  f.extend(y)
  c=1
  f2=list("FLAMES")
  fl=list("flames")
  for g in range(0,5):
   c-=1
   for a in range(0,len(f)):
    c+=1
    if c>len(fl):
     c=1
   fl.pop(c-1)
   print(fl)
   s=fl[0]
   if s=="f":
    l1.config(text="Friends")
    msg.config(text="Hey Dont Be Sad,Try To Devolop This Friendzone Into Something More")
   if s=="l":
    l1.config(text="Loves")
    msg.config(text="Looks Like You And Your Patner Are Madly In Love,If You Have'nt told Them How You Feel,Tell Them Now")
   if s=="a":
    l1.config(text="Affection")
    msg.config(text="Even Though You And Your Patner Are Not Madly In Love,Tell Them How You Feel About Them Now")
   if s=="m":
    l1.config(text="Married")
    msg.config(text="Looks Like You And Your Patner Got Your 'Happily Ever After'")
   if s=="e":
    l1.config(text="Enemies")
    msg.config(text="Hey Don't Feel Bad,This Is Just A Game I Am Sure You And Your Patner Get Your 'Happily Ever After',And If You Havent Told Them How You Feel About Then,Tell Them Now")
   if s=="s":
    l1.config(text="Sister")
    msg.config(text="Well Even Though Things May Look Bad,Remeber This Is Just for Fun,Prove To Your Patner That You Care About Them More Than These Silly Rituals")
  truth.mainloop()
your_name=Entry(width=25)
your_name.place(x=10,y=120)
patner_name=Entry(width=30)
patner_name.place(x=205,y=120)
plus=Label(text="+",font=("Aleo",25),bg="Pink2",fg="Red2")
plus.place(x=172,y=105)
equal=Button(text="=",bg="Pink2",fg="Red2",font=("Aleo",15),width=28,bd=2,command=opf)
equal.place(x=35,y=180)
def clm():
 main.destroy()
close=Button(text="Quit",command=clm,bg="Pink2",fg="Red2")
close.place(x=370,y=210)
main.mainloop()
