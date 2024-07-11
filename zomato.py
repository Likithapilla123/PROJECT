from tkinter import*
def generate():
    cb=200
    mb=400
    pb=300
    cc=150
    mc=300
    pc=200
    cbq=int(e1.get())
    mbq=int(e2.get())
    pbq=int(e3.get())
    ccq=int(e4.get())
    mcq=int(e5.get())
    pcq=int(e6.get())
    bill=(cb*cbq)+(mb*mbq)+(pb*pbq)+(cc*ccq)+(mc*mcq)+(pc*pcq)
    ob='Total Bill:'+str(bill)+'\n Thank you...visit Again!'
    l7.config(text=ob)
Zomato=Tk()
Zomato.title('Zomato')
Zomato.geometry('850x600')
l1=Label(Zomato,text='Enter no of chiken biryani packets:',font=('Times New Roman',16))
l2=Label(Zomato,text='Enter no of mutton biryani packets:',font=('Times New Roman',16))
l3=Label(Zomato,text='Enter no of prawns biryani packets:',font=('Times New Roman',16))
l4=Label(Zomato,text='Enter no of chiken curry packets:',font=('Times New Roman',16))
l5=Label(Zomato,text='Enter no of mutton curry packets:',font=('Times New Roman',16))
l6=Label(Zomato,text='Enter no of prawns curry packets:',font=('Times New Roman',16))
l7=Label(Zomato,text='',font=('Times New Roman',16))
e1=Entry(Zomato,font=('Times New Roman',16))
e2=Entry(Zomato,font=('Times New Roman',16))
e3=Entry(Zomato,font=('Times New Roman',16))
e4=Entry(Zomato,font=('Times New Roman',16))
e5=Entry(Zomato,font=('Times New Roman',16))
e6=Entry(Zomato,font=('Times New Roman',16))
b1=Button(Zomato,text='bill',font=('Times New Roman',16),command=generate)
l1.grid(row=0,column=0)
e1.grid(row=0,column=1)
l2.grid(row=1,column=0)
e2.grid(row=1,column=1)
l3.grid(row=2,column=0)
e3.grid(row=2,column=1)
l4.grid(row=3,column=0)
e4.grid(row=3,column=1)
l5.grid(row=4,column=0)
e5.grid(row=4,column=1)
l6.grid(row=5,column=0)
e6.grid(row=5,column=1)
b1.grid(row=6,column=0)
l7.grid(row=6,column=1)
mainloop()


