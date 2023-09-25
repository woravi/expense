from tkinter import *
from tkinter import ttk

GUI = Tk()
GUI.title('Pre-action System')
GUI.geometry('500x500')

L = Label(GUI, text='โปรแกรม Pre-action', font=('Angsana New', 30, 'bold'))
L.pack(pady=20)

#################################################### E1
L = Label(GUI, text='ราคาอาหาร', font=('Angsana New', 20))
L.pack(pady=5)

v_total = StringVar() #ตัวแปรพิเศษ เก็บข้อมูลเข้า GUI
E1 = ttk.Entry(GUI, font=('Angsana New', 25))
E1.pack(pady=10)

##################################################### E2
L = Label(GUI, text='จำนวนคน', font=('Angsana New', 20))
L.pack(pady=5)

v_person = StringVar()
E2 = ttk.Entry(GUI, font=('Angsana New', 25))
E2.pack(pady=10)

##################################################### บันทึก
B1 = ttk.Button(GUI, text='Calculator')
B1.pack(pady=10, ipadx=20, ipady=20)

GUI.mainloop()
