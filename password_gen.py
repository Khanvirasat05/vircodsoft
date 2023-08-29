from tkinter import*
import random
import string
from tkinter import messagebox


def gen_pass():
    length =entry2.get()
    if len(length) <= 0:
        pvar.set("")
        messagebox.showwarning("Alert!","Please enter a valid number")

    length = int(length)

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    pvar.set(password)

def reset():
    pvar.set("")


vir= Tk()
vir.geometry("550x420")
vir.title("Random Password Generator")

label1=Label(vir,text=" ",bg="sky blue")
label1.place(x=0,y=0,height=420,width=620)

label2=Label(vir,text="Password Generator",font=("calibre",15,"underline"),bg="sky blue")
label2.place(x=210,y=20)

label3=Label(vir,text="Enter user name:",font=("calibre"),bg="sky blue")
label3.place(x=40,y=100)

label4=Label(vir,text="Enter password length:",font=("calibre"),bg="sky blue")
label4.place(x=40,y=150)

pvar = StringVar()

label5=Label(vir,text="Generated Password:",font=("calibre"),bg="sky blue")
label5.place(x=40,y=200)

#Generate Button
button1=Button(vir,text="Generate Password",font=("calibre"),bg="sky blue",command=gen_pass)
button1.place(x=210,y=250,width=200)
button2=Button(vir,text="Reset",font=("calibre"),bg="sky blue",command=reset)
button2.place(x=230,y=300,width=150)

#creating entry boxes

entry1=Entry(vir,font=('italic',10, 'bold'),relief=GROOVE,bg="white")
entry1.place(x=250,y=105,height=30,width=250)

entry2=Entry(vir,font=('italic',10, 'bold'),relief=GROOVE,bg="white")
entry2.place(x=250,y=155,height=30,width=250)

entry3=Entry(vir,font=('italic',10, 'bold'),relief=GROOVE,bg="white",textvariable=pvar)
entry3.place(x=250,y=205,height=30,width=250)



vir.mainloop()