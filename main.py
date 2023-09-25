from tkinter import *
from tkinter import ttk

GUI = Tk()
GUI.geometry('500x500')
GUI.title('โปรแกรมหารกัน')
#########################
L = Label(GUI, text='ราคาอาหารทั้งหมด', font=('Angsana New', 15))
L.pack()

v_total = StringVar()
E1 = ttk.Entry(GUI, textvariable=v_total, font=('Angsana New', 20))
E1.pack()
#########################
L = Label(GUI, text='ทั้งหมดกี่คน', font=('Angsana New', 15))
L.pack()

v_person = StringVar()
E2 = ttk.Entry(GUI, textvariable=v_person, font=('Angsana New', 20))
E2.pack()


#########################

def Calculate():
    total = float(v_total.get())
    person = int(v_person.get())
    calc = total / person
    print('Split (baht/person): ', calc)

    text = 'รวมท้ังหมด{:,.2f} บาท จำนวน {} คน ({:,.2f} บาทต่อคน)'.format(total, person, calc)
    v_result.set(text)

    # from tkinter import messagebox
    # messagebox.showinfo('หารกันคนละ..', text)


B1 = ttk.Button(GUI, text='Calculate', command=Calculate)
B1.pack(pady=10, ipadx=20, ipady=10)

v_result = StringVar()
result = ttk.Label(GUI, textvariable=v_result, font=('Angsana New', 20, 'bold'), foreground='green')
result.pack(pady=10)


# def close():
#     GUI.quit()
# B2 = ttk.Button(GUI, text='X', width=5, command=close)
# B2.place(x=450, y=450)

GUI.mainloop()
