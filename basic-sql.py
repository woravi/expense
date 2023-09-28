# import sqlite3
#
# conn = sqlite3.connect('db.sqlite3')
# c = conn.cursor()
#
# c.execute("""CREATE TABLE IF NOT EXISTS expense (
#             ID INTEGER PRIMARY KEY AUTOINCREMENT,
#             title TEXT,
#             price REAL,
#             date TEXT)""")
#
#
# def insert_expense(title, price, date):
#     with conn:
#         command = 'INSERT INTO expense VALUES (?,?,?,?)'
#         c.execute(command, (None, title, price, date))
#     conn.commit()  # บันทึก
#     print('saved')
#
# def view_all_expense():
#     with conn:
#         command = 'SELECT * FROM expense'
#         c.execute(command)
#         result = c.fetchall()
#         print(result)
#     return result
#
# def update_expense(ID, field, newvalue):
#     with conn:
#         command = 'UPDATE expense SET {} = (?) WHERE ID=(?)'.format(field)
#         c.execute(command, ([newvalue, ID]))
#     conn.commit()
#     print('updated')
#
# def delete_expense(ID):
#     with conn:
#         command = 'DELETE FROM expense WHERE ID=(?)'
#         c.execute(command, ([ID]))
#     conn.commit()
#     print('deleted')
#
# # delete_expense(2)
# # delete_expense(3)
# # update_expense(1, 'price', '50')
#
# data = view_all_expense()
# print(data[0][1], data[0][2])
