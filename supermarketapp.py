import tkinter as tk
from tkinter import ttk,messagebox
window=tk.Tk()
window.geometry('400x300')
window.title('annai supermaket')

a=tk.StringVar()
b=tk.StringVar()
c=tk.StringVar()

lblname=tk.Label(window,text='customer name')
lblname.place(x=50,y=50)
txtname=tk.Entry(window,textvariable=a)
txtname.place(x=150,y=50)

lblmobnum=tk.Label(window,text='mobile number')
lblmobnum.place(x=50,y=100)
txtmobnum=tk.Entry(window,textvariable=b)
txtmobnum.place(x=150,y=100)

lblcity=tk.Label(window,text='city')
lblcity.place(x=50,y=150)
city_combo = ttk.Combobox(window,values=["kumbakonam","trichy","madurai"],textvariable=c)
city_combo.place(x=150,y=150)

def submitform():
    if a.get()=='' or b.get()=='' or c.get()=='':
        messagebox.showerror(title='form error',message='all field should be entered')
    else:
        messagebox.showinfo(title='form success',message='details saved successfully')
        # print(a.get())
        # print(c.get())

btnsubmit=tk.Button(window,text='submit',command=submitform)
btnsubmit.place(x=70,y=200)
window.mainloop()