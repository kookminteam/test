error_count = 0

while True:
    if error_count == 3:
        break
    n = input()

    neg = False
    if n[0] == "-":
        neg = True
        n = n[1:]

    if len(n) > 20:
        error_count += 1
        print("너무 긴 입력입니다.")
        continue
    elif not n.isdigit():
        error_count += 1
        print("잘못된 입력입니다.")
        continue
    else:
        error_count = 0

        temp = ""
        index = 0
        for i in range(1, len(n) + 1):
            index = len(n) - i
            if i % 3 == 0:
                temp += n[index]
                if i != len(n):
                    temp += ","
            else:
                temp += n[index]
        if neg == True:
            temp += "-" 
        temp = temp[::-1]
        print(temp)
