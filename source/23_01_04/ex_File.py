import os
path = os.chdir("../AI/COG_ICT/data")
# print(path)
# print("경로", os.getcwd())

# ===== 1 =====

# infilename = input("입력 파일 이름: ")
# outfilename = input("출력 파일 이름: ")

# infile = open(infilename, "r")
# outfile = open(outfilename, "w")

# sum = 0
# count = 0

# line = infile.readline()
# while line != "" :
#     s = int(line)
#     sum += s
#     count += 1
#     line = infile.readline()

# outfile.write("총매출 = "+ str(sum)+"\n")
# outfile.write("평균 일매출 = "+ str(sum/count ))

# infile.close()
# outfile.close() 


# # ===== 2 =====

# import random

# guesses = ''
# turns = 10

# infile = open("words.txt", "r")
# lines = infile.readlines()
# word = random.choice(lines).strip()

# while turns > 0:
#     failed = 0
#     for char in word:
#         if char in guesses:
#             print(char, end="")
#         else:
#             print("_", end="")
#             failed += 1
#     if failed == 0:
#         print("사용자 승리")
#         break
#     print("")
#     guess = input("단어를 추측하시오: ")
#     guesses += guess
#     if guess not in word:
#         turns -= 1
#         print ("틀렸음!")
#         print (str(turns)+ "기회가 남았음!")
#         if turns == 0:
#             print("사용자 패배 정답은 "+word)

# infile.close() 


# # ===== 3 =====

# filename = input("파일명을 입력하시오: ").strip()
# infile = open(filename + ".txt", "r")

# freqs = {}

# for line in infile:
#     for char in line.strip():
#         if char in freqs:
#             freqs[char] += 1
#         else:
#             freqs[char] = 1

# print(sorted(freqs.items()))
# infile.close()


# # ===== 4 =====

# filename = input("파일 이름을 입력하시오: ").strip()
# infile = open(filename + ".txt", "r")

# line_num = int(input("행 번호를 입력하시오: "))

# cnt = 1
# for line in infile:
#     if (line_num == cnt):
#         print(line.strip())
#     cnt += 1 


# # ===== 5 =====

# filename = input("파일 이름을 입력하시오: ").strip()
# infile = open(filename + ".txt", "r")

# max_len = 0

# for line in infile:
#     l = line.strip()
#     if max_len < len(l):
#         res = l
#         max_len = len(l)

# print(res)


# # ===== 6 =====

# filename = input("파일 이름을 입력하시오: ").strip()
# file = open(filename + ".txt", "r")


# freq = {}

# for line in file:
#     for word in line.lower().split():
#         freq[word] = freq.get(word, 0) + 1

# print(sorted(freq.items()))


# # ===== 7 =====

# import random

# fout = open("numbers.txt", "w")

# for _ in range(10):
#     # file.write(str(random.randint(1, 100)) + "\n")
#     print(random.randint(1, 100), file=fout)
# fout.close()

# fin = open("numbers.txt", "r")

# total = 0
# for line in fin:
#     total += int(line.strip())

# print(total//10)
    

# # ===== 8 =====

# os.mkdir("../AI/COG_ICT/data/tmp")
# os.chdir("../AI/COG_ICT/data/tmp")

# for ch in range(65, 91):
#     fname = chr(ch) + ".txt"
#     file = open(fname, 'w')
#     print(fname, file=file)
#     file.close()


# ===== 9 =====

import getpass
import hashlib

file = open("user.txt", 'w')

while (True):
    id = input("ID 등록: ")

    if id == '0': break

    pw = getpass.getpass(prompt="암호 등록: ")
    encrypted = hashlib.sha256(pw.encode()).hexdigest()
    print(f"{id}:{pw}", file=file)

file = open("user.txt", 'r')

uid = input("ID: ")
upw = getpass.getpass(prompt="PW: ")
upw_encrypted = hashlib.sha256(upw.encode()).hexdigest()

for line in file:
    key, value = line.strip().split(':')
    if uid == key:
        if upw_encrypted == value:
            print(f"{uid}님 환영합니다.")
        else:
            print("암호가 틀렸습니다.")
        break
else:
    print("존재하지 않는 유저입니다.")









