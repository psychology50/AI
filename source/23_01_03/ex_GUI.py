from tkinter import *

window = Tk()

# ===== 1 =====

# Label(window, text="너비").grid(row=0, column=0)
# Label(window, text="높이").grid(row=1, column=0)

# e1 = Entry(window)
# e2 = Entry(window)

# e1.grid(row=0, column=1)
# e2.grid(row=1, column=1)

# photo = PhotoImage(file="19.gif")
# label = Label(window, image=photo)
# label.grid(row=0, column=2, columnspan=2, rowspan=2)

# Button(window, text="증가").grid(row=2, column=0, columnspan=2)

# Button(window, text="확대").grid(row=2, column=2)
# Button(window, text="축소").grid(row=2, column=3)

# window.mainloop()


# # ===== 2 =====

# Label(window, text="화씨").grid(row=0, column=0)
# Label(window, text="섭씨").grid(row=1, column=0)

# e1 = Entry(window)
# e2 = Entry(window)

# e1.grid(row=0, column=1)
# e2.grid(row=1, column=1)

# def ftoc():
#     tf = float(e1.get())
#     tc = (tf-32.0) * 5.0/9.0
#     e2.delete(0, END)
#     e2.insert(0, str(tc))

# def ctof():
#     tc = float(e2.get())
#     tf = tc * 1.8
#     e1.delete(0, END)
#     e1.insert(0, str(round(tf, 2)))

# def reset():
#     e1.delete(0, END)
#     e2.delete(0, END)
#     e1.focus_set()

# Button(window, text="화씨->섭씨", command=ftoc).grid(row=2, column=0)
# Button(window, text="섭씨->화씨", command=ctof).grid(row=2, column=1, sticky=E+W)
# Button(window, text="Reset", command=reset).grid(row=3, column=0, columnspan=2, sticky=E+W)

# window.mainloop()


# # ===== 3 =====

# import random # rock_paper_scissor.py

# Label(window, text="선택하세요", font=("Helvetica", "16")).pack()
# frame = Frame(window)

# rock_image = PhotoImage(file="rock.png")
# paper_image = PhotoImage(file="paper.png")
# scissors_image = PhotoImage(file="scissors.png")

# def decide(human):
#     computer = random.choice(["가위", "바위", "보"])
#     if computer == "바위":
#         computer_image["image"] = rock_image
#     elif computer == "보":
#         computer_image["image"] = paper_image
#     else:
#         computer_image["image"] = scissors_image
#     if (computer == "바위" and human == "보") or (computer == "보" and human == "가위") or (computer == "가위" and human == "바위"):
#         result = "인간 승리!"
#     elif computer == human:
#         result = "비겼습니다."
#     else:
#         result = "컴퓨터 승리!"
#     output.config(text="인간: " + human + " 컴퓨터:" + computer + " " + result)

# def pass_s():
#     user_image["image"] = scissors_image
#     decide("가위")
# def pass_r():
#     user_image["image"] = rock_image
#     decide("바위")
# def pass_p():
#     user_image["image"] = paper_image
#     decide("보")

# rock = Button(frame, image=rock_image, command=pass_r)
# rock.pack(side="left")
# paper = Button(frame, image=paper_image, command=pass_p)
# paper.pack(side="left")
# scissors = Button(frame, image=scissors_image, command=pass_s)
# scissors.pack(side="left")

# frame.pack()

# frame2 = Frame(window)

# computer_image = Label(frame2)
# user_image = Label(frame2)

# computer_image.pack(side='left', padx = 30)
# user_image.pack(side='left', padx = 30)

# output = Label(window, text="", font=("Helvetica", "16"))
# output.pack()

# window.mainloop()


# # ===== 4 =====

# def checked(i):
#     global player
#     button = list[i] # 리스트에서 i번째 버튼 객체를 가져온다. 
    
#     # 버튼이 초기상태가 아니면 이미 누른 버튼이므로 아무것도 하지 않고 리턴한다.
#     if button["text"] != "          ":
#         return
#     button["text"] = "   " + player+ "    "
#     if player=="X":
#         player = "O"
#         button["bg"] = "yellow"
#     else :
#         player = "X"
#         button["bg"] = "lightgreen"

# def is_terminated(i):
#     row = i // 3
#     col = i % 3
#     text = list[i]["text"]

#     for c in range(3):
#         if list[row*3 + c]["text"] != text:
#             break
#     # else:


# player="X" # 시작은 플레이어 X이다.
# list = []

# # 9개의 버튼을 생성하여 격자 형태로 윈도우에 배치한다.
# for i in range(9):
#     b = Button(window, text=" ", command=lambda k=i: checked(k))
#     b.grid(row=i//3, column=i%3)
#     list.append(b) # 버튼 객체를 리스트에 저장한다. 
    
# window.mainloop()


# # ===== 5 =====

# # def click:

# import random

# window.geometry("300x300")
# window.title("주사위 굴리기")

# def click():
#     label["text"] = str(random.randint(1,6))

# label = Label(window, text="1", font=("Arial", 100, "bold"), fg="red")
# btn = Button(window, command=click, text="굴리기", font=("Arial", 20, "bold"), fg="blue")
# label.pack(side="left", padx=50)
# btn.pack(side="right")

# window.mainloop()


# # ===== 6 =====

# def process():
#     for x in range(3):
#         print(f"{label[x]} = {form[x].get()}")

# def clear():
#     for x in range(3):
#         form[x].delete(0, END)
#     form[0].focus_set()

# label = ["이름", "직업", "나이"]
# form = []

# for e in range(3):
#     Label(window, text=label[e], font=("Arial", 14), padx=15).grid(row=e, column=0)
#     form.append(Entry(window, font=("Arial", 14)))
#     form[e].grid(row=e, column=1, columnspan=2)

# frame = Frame(window)
# frame.grid(row=3, column=1)

# Button(frame, text="처리", command=process, font=("Arial", 14)).pack(side="left")
# Button(frame, text="다시 입력", command=clear, font=("Arial", 14)).pack(side="left")

# window.mainloop()


# ===== 7 =====

WIDTH = 600
HEIGHT = 200
def displayRect():
    canvas.create_rectangle(10,10,WIDTH-10,HEIGHT-10)
def displayOval():
    canvas.create_oval(10,10,WIDTH-10,HEIGHT-10, fill="yellow")
def displayArc():
    canvas.create_arc(10,10,WIDTH-10,HEIGHT-10,start=30,
    extent=300,width=10,fill='blue')
def displayPolygon():
    canvas.create_polygon(10,10,WIDTH-10,HEIGHT-10,200,90,300, 160)
def displayLine():
    canvas.create_line(10,10,WIDTH-10,HEIGHT-10,fill='green')
def clearCanvas():
    canvas.delete(ALL)

canvas=Canvas(window, width=WIDTH, height=HEIGHT, bg='white')
canvas.pack()
frame=Frame(window)
frame.pack()
btLine=Button(frame, text="Line",command=displayLine).grid(row=1,column=1)
btRectangle=Button(frame, text="Rectangle", command=displayRect).grid(row=1,column=2)
btOval=Button(frame,text="Oval",command=displayOval).grid(row=1,column=3)
btPolygon=Button(frame, text="Polygon",command=displayPolygon).grid(row=1,column=4)
btArc=Button(frame, text="Arc",command=displayArc).grid(row=1,column=5)
btClear=Button(frame,text="Clear",command=clearCanvas).grid(row=1,column=7)
window.mainloop()

