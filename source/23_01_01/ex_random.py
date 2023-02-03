import random

user = int(input("가위 1, 바위 2, 보 3 : "))
com = random.randint(1, 3)

str = ["가위", "바위", "보"]

print(f"user는 {str[user-1]} com는 {str[com-1]}을 냈습니다. ")
if (user == 1 and com == 3) or (user == 2 and com == 1) or (user == 3 and com == 2):
    print("이겼습니다.")
elif (user == com):
    print("비겼습니다.")
else:
    print("졌습니다.")
