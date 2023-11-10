import tkinter as tk
from tkinter import messagebox
window=tk.Tk()
window.geometry('300x400')
window.title('calc')

a=tk.StringVar()
b=tk.StringVar()

lbluser=tk.Label(window,text='username')
lbluser.place(x=50,y=50)
txtuser=tk.Entry(window,textvariable=a)
txtuser.place(x=150,y=50)

lblpass=tk.Label(window,text='password')
lblpass.place(x=50,y=100)
txtpass=tk.Entry(window,show='*',textvariable=b)
txtpass.place(x=150,y=100)

def login():
    if a.get()=='' or b.get()=='':
        # print('username or password should not be empty')
        messagebox.showerror(title='error',message='username or password should not be empty')

btnsubmit=tk.Button(window,text='submit',command=login)
btnsubmit.place(x=50,y=200)
window.mainloop()