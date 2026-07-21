from tkinter import*
def C():
    global tekst
    tekst=""
    var.set(tekst)
def f(numer):
    global tekst
    tekst=tekst+str(numer)
    var.set(tekst)
def rownasie():
    global tekst
    wynik=str(eval(tekst))
    var.set(wynik)
    tekst=str(wynik)
przycisk=Tk()
var=StringVar()
Ekran=Entry(przycisk,bd=30,justify="right",textvariable=var).grid(columnspan=4)  
tekst="" 
przycisk1=Button(przycisk,padx=14,bd=8,text="1",command=lambda:f(1)).grid(row=3,column=0)
przycisk2=Button(przycisk,padx=14,bd=8,text="2",command=lambda:f(2)).grid(row=3,column=1)
przycisk3=Button(przycisk,padx=14,bd=8,text="3",command=lambda:f(3)).grid(row=3,column=2)
przycisk4=Button(przycisk,padx=14,bd=8,text="4",command=lambda:f(4)).grid(row=2,column=0)
przycisk5=Button(przycisk,padx=14,bd=8,text="5",command=lambda:f(5)).grid(row=2,column=1)
przycisk6=Button(przycisk,padx=14,bd=8,text="6",command=lambda:f(6)).grid(row=2,column=2)
przycisk7=Button(przycisk,padx=14,bd=8,text="7",command=lambda:f(7)).grid(row=1,column=0)
przycisk8=Button(przycisk,padx=14,bd=8,text="8",command=lambda:f(8)).grid(row=1,column=1)
przycisk9=Button(przycisk,padx=14,bd=8,text="9",command=lambda:f(9)).grid(row=1,column=2)
przycisk0=Button(przycisk,padx=14,bd=8,text="0",command=lambda:f(0)).grid(row=4,column=0)
dodac=Button(przycisk,padx=14,bd=8,text="+",command=lambda:f("+")).grid(row=1,column=3)
odjac=Button(przycisk,padx=14,bd=8,text="-",command=lambda:f("-")).grid(row=2,column=3)
razy=Button(przycisk,padx=14,bd=8,text="*",command=lambda:f("*")).grid(row=3,column=3)
podzielic=Button(przycisk,padx=14,bd=8,text="/",command=lambda:f("/")).grid(row=4,column=3)
wyczysc=Button(przycisk,padx=14,bd=8,text="C",command=lambda:C()).grid(row=4,column=2)
rowna=Button(przycisk,padx=14,bd=8,text="=",command=lambda:rownasie()).grid(row=4,column=1)
przycisk.mainloop() 