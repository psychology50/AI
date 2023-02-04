# # ===== 1 =====

# import math

# class Circle:
#     def __init__(self, r):
#         self.r = r
    
#     def getArea(self):
#         return math.pi * self.r ** 2

#     def getPerimiter(self):
#         return 2 * math.pi * self.r

# c = Circle(10)
# print(c.getArea())
# print(c.getPerimiter())


# # ===== 2 =====

# # 변수 앞에 __ 가 붙으면 수정 불가능하다

# class Student:
#     def __init__(self, age, name):
#         self.__age = age
#         self.__name = name

# obj = Student(10, "양재서") 
# # print(obj.__name) // 에러 발생!!!!
# print(dir(obj)) # 클래스 속성 출력
# print(obj._Student__age) # 보려면 볼 수는 있다. private라고 하기에는 다소 허술하다.


# # ===== 3 =====

# class BankAccount:
#     def __init__(self, balance):
#         self.__balance = balance
    
#     def deposit(self, value):
#         self.__balance += value
#         print(f"{value}원이 입금되었습니다. 잔고 = {self.__balance}원")

#     def withdraw(self, value):
#         if self.__balance - value < 0:
#             print(f"잔액이 부족합니다. 잔고 = {self.__balance}원")
#         else:
#             self.__balance -= value
#             print(f"{value}원이 출금되었습니다. 잔고 = {self.__balance}원")
    
# ba = BankAccount(5000)
# ba.deposit(100)
# ba.withdraw(4000)
# ba.withdraw(4000)


# # ===== 4 =====

# class Rocket:
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y

#     def __str__(self):
#         return f"로켓의 위치 = ({self.x}, {self.y})"

#     def moveUp(self):
#         self.y += 1

#     def goto(self, x, y):
#         self.x = x
#         self.y = y

# rocket = Rocket()
# print(rocket)
# rocket.moveUp()
# print(rocket)
# rocket.goto(100, 200)
# print(rocket)


# # ===== 5 =====

# class Stack:
#     def __init__(self):
#         self.__data = []
    
#     def push(self, e):
#         self.__data.append(e)

#     def pop(self):
#         if self.__data:
#             d = self.__data[-1]
#             del self.__data[-1]
#             return d
#         else:
#             return None

#     def top(self):
#         if self.__data:
#             return self.__data[-1]
#         else:
#             return None
    
#     def __len__(self):
#         return len(self.__data)

# S = Stack()
# S.push(1)
# S.push(5)
# S.push(3)
# print(len(S))
# print(S.pop())
# print(S.top())


# # ===== 6 =====

# list1 = []
# list2 = []
# list3 = []

# print(list1 == list2)
# print(list1 is list2)
# print(list1 is list3)

# list3 += list2
# print(list1 is list3)
# print(list1 == list3)


# # ===== 7 =====

# class Vector2D:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b

#     def __str__(self):
#         return f"({self.a}, {self.b})"

#     def __add__(self, other):
#         return Vector2D(self.a + other.a, self.b + other.b)

#     def __sub__(self, other):
#         return Vector2D(self.a - other.a, self.b - other.b)

#     def __eq__(self, other):
#         return self.a == other.a and self.b == other.b

#     def __gt__(self, other):
#         return self.a ** 2 + self.b ** 2 > other.a ** 2 + other.b ** 2

#     def __repr__(self):
#         return f"({self.a}, {self.b})"


# u = Vector2D(0, 1)
# v = Vector2D(1, 0)
# a = u + v
# print(a)
# print(a > v)

# import random

# A = []
# for _ in range(10):
#     A.append(Vector2D(random.randint(0, 9), random.randint(0, 9)))
# print(A)

# print(sorted(A)) ## __gt__를 기준으로 정렬
# print(sorted(A, reverse=True))


# # ===== 8 =====

# class Rectangle:
#     def __init__(self, x, y, w, h):
#         self.x = x
#         self.y = y
#         self.w = w
#         self.h = h

#     def __str__(self):
#         return f"좌측 하단 : ({self.x}, {self.y}), 너비와 높이: ({self.w} * {self.h})"

#     def __gt__(self, other):
#         return self.w * self.h > other.w * other.y

#     def oberlap(self, other):
#         if not (self.x + self.w >= other.x or self.x <= other.x + other.w):
#             return False
#         if not (self.y + self.h >= other.y or self.y <= other.y + other.h):
#             return False
#         return True


# # ===== 9 =====

# class PhoneBook:
#     def __init__(self):
#         self.contact = []

#     def add(self, name, phone=None, email=None):
#         self.contact.append({"name": name, "phone": phone, "email": email})

#     def get(self, name):
#         for user in self.contact:
#             if user.get("name") == name:
#                 return user.get("phone"), user.get("email")

#     def __str__(self):
#         res = ""
#         for user in self.contact:
#             res += f"{user.get('name')}\n전화번호: {user.get('phone')}\n이메일: {user.get('email')}\n"
#         return res

# pb = PhoneBook()
# pb.add("Cho", "010-1234-5678", "cho@naver.com")
# pb.add("Kim", "010-1111-2222", "kim@naver.com")
# print(pb)
# print(pb.get("Cho"))


# ===== 10 =====



        


