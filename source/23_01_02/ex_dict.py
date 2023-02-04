# ===== 1 =====
# import random

# D = {chr(ord('A') + x) : random.randint(1000, 9999) for x in range(26)}
# print(D)

# id = input()
# print(f"사용자의 비밀번호는 {D.get(id)}입니다.")


# ===== 2 =====

# I = input()
# D = {}

# for i in I:
#     if D.get(i) == None:
#         D[i] = 1
#     else:
#         D[i] += 1

# print(D)


# # ===== 3 =====

# import random

# A = {}
# for i in range(1000):
#     key = random.randint(1, 6)
#     A[key] = A.get(key) + 1

# print(sorted(A.items(), key = lambda x: x[1]))


# # ===== 4 =====
# import random

# alphabet = [chr(ord('a') + x) for x in range(26)]
# random.shuffle(alphabet)
# print(alphabet)

# D = {chr(ord('a') + x) : alphabet[x] for x in range(26)}

# txt = input()
# encryted = ""
# for ch in txt:
#     if ch in D:
#         encryted += D[ch]
#     else:
#         encryted += ch
# print(f"암호문 : {encryted}")
