from tkinter import *
from tkinter import ttk
from datetime import datetime
import csv


def writecsv(data):
    with open('data.csv', 'a', newline='', encoding='utf-8') as file:
        fw = csv.writer(file)
        fw.writerow(data)


GUI = Tk()
GUI.geometry('500x500')
GUI.title('โปรแกรมบันทึกค่าใช้จ่าย')

FONT1 = ('Angsana New', 20)

FT1 = Frame()
FT1.place(x=50, y=50)

################### config TAP #####################
TAP = ttk.Notebook(GUI)
TAP.pack(fill=BOTH, expand=1)

T1 = Frame(TAP)
T2 = Frame(TAP)

icon_tap1 = PhotoImage(file='tap1.png')
icon_tap2 = PhotoImage(file='tap2.png')

TAP.add(T1, text='บันทึกค่าใช้จ่าย', image=icon_tap1, compound='top')
TAP.add(T2, text='ประวัติค่าใช้จ่าย', image=icon_tap2, compound='top')

#################   TAP1  ##################
iconImage = PhotoImage(file='expense.png')
L = Label(T1, image=iconImage)
L.pack()

# ช่องรายการบันทึก
L = Label(FT1, text='รายการค่าใช้จ่าย', font=(None, 30))
L.pack(pady=5)
v_expense = StringVar()
E1 = ttk.Entry(T1, textvariable=v_expense, font=FONT1)
E1.pack()

# ช่องจำนวนเงิน!
L = Label(T1, text='จำนวนเงิน (บาท)', font=(None, 30))
L.pack()
v_amount = StringVar()
E2 = ttk.Entry(T1, textvariable=v_amount, font=FONT1)
E2.pack()


# ปุ่มบันทึก
def SaveData(event=None):
    expense = v_expense.get()
    amount = float(v_amount.get())
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    data = [expense, amount, timestamp]
    writecsv(data)
    v_expense.set('')
    v_amount.set('')
    E1.focus()


E2.bind('<Return>', SaveData)  # event = None
E1.bind('<Return>', lambda x: E2.focus())  # ฟังชั่นพิเศษ bind โดยไม่ต้องสร้างฟังชั่น

B1 = ttk.Button(T1, text="บันทึก", command=SaveData)
B1.pack()

#################################


GUI.mainloop()
