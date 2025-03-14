from tkinter import *
from tkinter import messagebox
import database1

db1 = database1.Database('c:/zahra/database.db')


win = Tk()
win.geometry('500x350')
win.title('Login Form ')
win.configure(bg='black')
win.resizable(0,0)


#===== funk 
def clear():
    ent_n.delete(0, END)
    ent_ln.delete(0, END)
    ent_e.delete(0, END)
    ent_p.delete(0, END)
    ent_n.focus_set()


def sign_up():
    fname=ent_n.get()
    lname=ent_ln.get()
    email=ent_e.get()
    password=ent_p.get()
    if email == '' or password == '':
        messagebox.showerror('Error','You should input data!')
        return
    else:
        db1.insert(fname, lname, email, password)
        messagebox.showinfo('Success','You add successfully!')
        clear()


def sign_in():
    email = ent_e.get()
    password = ent_p.get()
    if email == '' or password == '':
        messagebox.showerror('Error!', 'Email and Password are required!')
        return
    else:
        data = db1.search(email, password)
        if data:
            messagebox.showinfo('Welcome', f'{data[0]} {data[1]}, welcome!')
            clear()
        else:
            messagebox.showerror('Error', 'Invalid email or password !')


#======== view
lbl_n = Label(win,text='Fname: ',font='Dubai 13').place(x=95,y=10)
lbl_ln = Label(win,text='Lname: ',font='Dubai 13').place(x=95,y=50)
lbl_e = Label(win,text='Email: ',font='Dubai 13',width=5).place(x=95,y=90)
lbl_p = Label(win,text='Password: ',font='Dubai 13').place(x=95,y=130)

ent_n = Entry(win,font='Dubai 10')
ent_n.place(x=180,y=10)
ent_ln = Entry(win,font='Dubai 10')
ent_ln.place(x=180,y=55)
ent_e = Entry(win,font='Dubai 10')
ent_e.place(x=180,y=95)
ent_p = Entry(win,font='Dubai 10')
ent_p.place(x=180,y=135)

btn_su = Button(win,text='Sing Up',width=20,command=sign_up)
btn_su.place(x=90,y=250)
btn_su = Button(win,text='Sing In',width=20,command=sign_in)
btn_su.place(x=280,y=250)

lbl_s1 = Label(win,text='*',font='Dubai 13').place(x=85,y=90)
lbl_s2 = Label(win, text='*', font='Dubai 13').place(x=85,y=130)

win.mainloop()