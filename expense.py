from tkinter import *
from tkinter import ttk
from datetime import datetime
import csv
#############################################
import sqlite3

conn = sqlite3.connect('db.sqlite3')
c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS expense (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            price REAL,
            date TEXT)""")


def insert_expense(title, price, date):
    with conn:
        command = 'INSERT INTO expense VALUES (?,?,?,?)'
        c.execute(command, (None, title, price, date))
    conn.commit()  # บันทึก
    print('saved')


def view_all_expense():
    with conn:
        command = 'SELECT * FROM expense'
        c.execute(command)
        result = c.fetchall()
        print(result)
    return result


def update_expense(ID, field, newvalue):
    with conn:
        command = 'UPDATE expense SET {} = (?) WHERE ID=(?)'.format(field)
        c.execute(command, ([newvalue, ID]))
    conn.commit()
    print('updated')


def delete_expense(ID):
    with conn:
        command = 'DELETE FROM expense WHERE ID=(?)'
        c.execute(command, ([ID]))
    conn.commit()
    print('deleted')


#############################################

def writecsv(data):
    with open('data.csv', 'a', newline='', encoding='utf-8') as file:
        fw = csv.writer(file)
        fw.writerow(data)


def readcsv():
    with open('data.csv', newline='', encoding='utf8') as file:
        fr = list(csv.reader(file))
        # print(fr)
    return fr


GUI = Tk()
GUI.geometry('800x800')
GUI.title('โปรแกรมบันทึกค่าใช้จ่าย')

FONT1 = ('Angsana New', 20)

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
FT1 = Frame(T1)
FT1.place(x=250, y=50)

iconImage = PhotoImage(file='expense.png')
L = Label(FT1, image=iconImage)
L.pack()

# ช่องรายการค่าใช้จ่าย
L = Label(FT1, text='รายการค่าใช้จ่าย', font=(None, 30))
L.pack(pady=5)

v_expense = StringVar()
E1 = ttk.Entry(FT1, textvariable=v_expense, font=FONT1)
E1.pack(pady=5)

# ช่องกรอกจำนวนเงินค่าใช้จ่าย
L = Label(FT1, text='จำนวนเงิน (บาท)', font=(None, 30))
L.pack(pady=5)

v_amount = StringVar()
E2 = ttk.Entry(FT1, textvariable=v_amount, font=FONT1)
E2.pack(pady=5)


# ปุ่มบันทึก

def update_table():
    #   Clear Table
    table.delete(*table.get_children())
    data = view_all_expense()
    for d in data:
        table.insert('', 'end', values=[d[0], d[1], d[2], d[3]])


def SaveData(event=None):
    expense = v_expense.get()
    amount = float(v_amount.get())
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    # data = [expense, amount, timestamp]
    # writecsv(data)

    insert_expense(expense, amount, timestamp)
    v_expense.set('')
    v_amount.set('')
    E1.focus()
    update_table()


E2.bind('<Return>', SaveData)  # event = None
E1.bind('<Return>', lambda x: E2.focus())  # ฟังชั่นพิเศษ bind โดยไม่ต้องสร้างฟังชั่น


def Fav1(event=None):
    v_expense.set('น้ำเต้าหู้')
    v_amount.set('15')


GUI.bind('<F1>', Fav1)

B1 = ttk.Button(FT1, text="บันทึก", command=SaveData)
B1.pack(ipadx=20, ipady=10, pady=5)

#######TABLE - EXPENSE######

header = ['ID', 'รายการ', 'ค่าใช้จ่าย', 'วัน-เวลา']
hwidth = [70, 300, 150, 170]

table = ttk.Treeview(T2, columns=header, show='headings', height=20)
table.place(x=40, y=20)

# resize
style = ttk.Style()
style.configure('Treeview.Heading', font=(None, 15))
style.configure('Treeview', font=(None, 13), rowheight=30)


table.column('ค่าใช้จ่าย', anchor=E)
table.column('รายการ', anchor=CENTER)

for h, w in zip(header, hwidth):
    table.column(h, width=w)
    table.heading(h, text=h)

# table.insert('', 'end', values=['A', 'B', 'C', 'D'])
# data = readcsv()

data = view_all_expense()

for i, d in enumerate(data, start=1):
    # d.insert(0, i)
    # table.insert('', 'end', values=d)
    # d.insert(0,i) แบบนี้ก็ได้
    table.insert('', 'end', values=[d[0], d[1], d[2], d[3]])


# delete

def delete_data(event):
    select = table.selection()
    print(select)
    select_data = table.item(select)
    print(select_data['values'][0])
    ID = select_data['values'][0]
    check = messagebox.askyesno('ยืนยันการลบ','คุณต้องการลบข้อมูลไช่หรือไม่','ลบแล้วไม่สามารถกู้คืนได้')
    print([check],type(check))
    if check:
        delete_expense(ID)
        update_table()

def update_data(event):
    select = table.selection()
    select_data = table.item(select)
    ID = select_data['values'][0]
    title = select_data['values'][1]
    price = select_data['values'][2]

    GUI2 = Toplevel()
    GUI2.geometry('800x700')
    GUI2.title('แก้ไขรายการ')

    L = Label(GUI2, text='รายการค่าใช้จ่าย', font=(None, 30))
    L.pack(pady=5)

    v_expense2 = StringVar()
    v_expense2.set(title)
    E1 = ttk.Entry(GUI2, textvariable=v_expense2, font=FONT1)
    E1.pack(pady=5)
    # ช่องจำนวนเงิน!
    L = Label(GUI2, text='จำนวนเงิน (บาท)', font=(None, 30))
    L.pack(pady=5)

    v_amount2 = StringVar()
    v_amount2.set(price)
    E2 = ttk.Entry(GUI2, textvariable=v_amount2, font=FONT1)
    E2.pack(pady=5)

    def UpdateData():
        update_expense(ID, 'title', v_expense2.get())
        update_expense(ID, 'price', float(v_amount2.get()))
        update_table()
        GUI2.destroy()

    B1 = ttk.Button(GUI2, text="บันทึก", command=UpdateData)
    B1.pack(ipadx=20, ipady=10, pady=5)

    GUI2.mainloop()


table.bind('<Double-1>',update_data)
table.bind('<Delete>',delete_data) # don't forget 'event' in function

GUI.mainloop()
