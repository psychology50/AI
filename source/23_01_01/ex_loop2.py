str = input("문장을 입력하세요: ")

alpha = num = space = 0
for c in str:
    if '0' <= c <= '9':
        num += 1
    elif c == '\t' or c == '\n' or c == " ":
        space += 1
    else:
        alpha += 1
print(f"알파벳 문자의 수 = {alpha}\n숫자 문자의 수 = {num}\n공백 문자의 수 = {space}")
