x = int(input('請輸入一個正整數：'))
candidate = 1
prime = []
while candidate <= x:
    factor = []
    i = 1
    while i <= candidate:
        if candidate % i == 0:
            factor.append(i)
        i += 1
    if len(factor) == 2:
        prime.append(candidate)
    candidate += 1
print(x, '以內的質數有', prime)
