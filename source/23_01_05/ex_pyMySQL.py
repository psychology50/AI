# import pymysql

# mydb = pymysql.connect(host="127.0.0.1", user="root", passwd="aespa0519", port=3330, db="StudentDB")
# mc = mydb.cursor()

# ===== test =====
# mc.execute("select * from student")
# result = mc.fetchall()
# print(result)

# mc.execute("select * from department")
# print(mc.fetchone())
# print(mc.fetchone())
# print(mc.fetchone())


# ===== create table =====

# sql = "create table logs (id int auto_increment primary key,\
#                           type int,\
#                           place varchar(40),\
#                           time datetime)"
# mc.execute(sql)
# mydb.commit()

# mc.execute("show tables")

# for x in mc:
#     print(x)


# ===== insert =====

# import datetime

# sql = "INSERT INTO logs(type, place, time) value = (%s, %s, %s)"
# value = (8, '대구', datetime.datetime())
# mc.execute(sql, value)
# mydb.commit()


# import random

# places = ['대구', '서울', '부산', '울산', '광주', '인천', '대전']
# types = list(range(1, 11))
# val = [(random.choice(types), 
#         places[random.randint(0, 6)], 
#         datetime.datetime.now() + datetime.timedelta(days=random.randint(-1000, 0),
#                                                      hours=random.randint(-12, 12),
#                                                      seconds=random.randint(0, 3600)))\
#         for _ in range(100)]

# sql = "INSERT INTO logs(type, place, time) VALUES (%s, %s, %s)"
# mc.executemany(sql, val)
# mydb.commit()
# print(mc.rowcount, 'record insert')
# mc.execute("select * from logs")

# for x in mc:
#     print(x)



# # ===== 3 ===== 

# import pymysql
# from tkinter import *
# import pickle
# import tkinter.messagebox

# mydb = pymysql.connect(host="127.0.0.1", user="root", passwd="aespa0519", port=3330, db="StudentDB")
# mc = mydb.cursor()

# class STUDENT:
#     def receive(self):
#         sql = "select * from student where sid = %s"
#         value = (form[0].get(), )
#         mc.execute(sql, value)
#         res = mc.fetchone()
#         for x in range(8):
#             form[x].delete(0, END)
#             form[x].insert(0, res[x])
            
#     def create(self):
#         try:
#             sql = "INSERT INTO student VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
#             value = [form[x].get() for x in range(8)]
#             mc.execute(sql, value)
#             mydb.commit()
#             tkinter.messagebox.showinfo(title="성공", message="정보가 성공적으로 저장되었습니다.")
#             self.reset()
#         except pymysql.err.DatabaseError as e:
#             tkinter.messagebox.showinfo(title="오류", message=set(e))

#     def update(self):
#         pass

#     def delete(self):
#         sql = "DELETE FROM student where sid = %s"
#         value = (form[0].get(), )
#         mc.execute(sql, value)
#         tkinter.messagebox.showinfo(title="성공", message="정보가 성공적으로 삭제되었습니다.")

#     def reset(self):
#         for x in range(8):
#             form[x].delete(0, END)
#         form[0].focus_set()

# window = Tk()
# st = STUDENT()

# label = ["학번", "이름", "학과", "지도교수", "성별", "주소", "생일", "학점"]
# form = []

# for e in range(8):
#     Label(window, text=label[e], font=("Arial", 14), padx=15).grid(row=e, column=0)
#     form.append(Entry(window, font=("Arial", 14)))
#     form[e].grid(row=e, column=1, columnspan=2)

# frame = Frame(window)
# frame.grid(row=8, column=1)

# Button(frame, text="검색", command=st.receive, font=("Arial", 14)).pack(side="left")
# Button(frame, text="추가", command=st.create, font=("Arial", 14)).pack(side="left")
# Button(frame, text="수정", command=st.update, font=("Arial", 14)).pack(side="left")
# Button(frame, text="삭제", command=st.delete, font=("Arial", 14)).pack(side="left")
# Button(frame, text="다시 입력", command=st.reset, font=("Arial", 14)).pack(side="left")

# window.mainloop()


# ===== 4 =====




