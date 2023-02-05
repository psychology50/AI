import os
path = os.chdir("../AI/COG_ICT/data")

# ===== 1 =====

# import pickle
# import random

# A = [random.randint(1, 101) for _ in range(10)]

# file = open("pf.dat", "wb")
# obj = pickle.dump(A, file)
# file.close()

# fin = open("pf.dat", "rb")
# B = pickle.load(fin)

# print(A)
# print(B)
# print(A == B)

# def dump(fname, container):
#     file = open(fname, "ab")
#     pickle.dump(container, file)
#     file.close()

# dump("pf.dat", {"이순신", "강감찬", "을지문덕"})
# dump("pf.dat", {1:'A', 2:'B', 3:'C'})
# dump("pf.dat", tuple(x*x for x in range(10, 100, 10)))

# file = open("pf.dat", "rb")
# A = pickle.load(file)
# print(A)
# print(A)
# print(A)


# # ===== 2 =====

# import pickle

# file = open("pf.dat", "rb")

# A = []

# try:
#     while True:
#         A.append(pickle.load(file))
# except EOFError:
#     file.close()

# print(A)


# ===== 3 =====

from tkinter import *
import pickle
import tkinter.messagebox

def dump(fname, container):
    file = open(fname, "ab")
    pickle.dump(container, file)
    file.close()

def load(fname):
    file = open(fname, "rb")
    return pickle.load(file)
    

def process():
    d = {}
    d[form[0].get()] = {form[1].get(), form[2].get()}
    dump("user.dat", d)
    tkinter.messagebox.showinfo(title="성공", message="정보가 성공적으로 저장되었습니다.")
    clear()
        
def clear():
    for x in range(3):
        form[x].delete(0, END)
    form[0].focus_set()

def floor():
    res = load("user.dat")
    print(res)

window = Tk()

label = ["이름", "직업", "나이"]
form = []

for e in range(3):
    Label(window, text=label[e], font=("Arial", 14), padx=15).grid(row=e, column=0)
    form.append(Entry(window, font=("Arial", 14)))
    form[e].grid(row=e, column=1, columnspan=2)

frame = Frame(window)
frame.grid(row=3, column=1)

Button(frame, text="저장", command=process, font=("Arial", 14)).pack(side="left")
Button(frame, text="다시 입력", command=clear, font=("Arial", 14)).pack(side="left")
Button(frame, text="파일 내용 출력", command=floor, font=("Arial", 14)).pack(side='left')

window.mainloop()

