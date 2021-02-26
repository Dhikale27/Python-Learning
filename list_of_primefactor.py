x = int(input("enter number: "))
pf = [1]
for num in range(2, x):
    if x % num == 0:
        for i in range(2,num +1):
            if i < num:
                if num % i == 0:
                    pass
                    break
                else:
                    i += 1
            else:
                pf.append(num)

    else:
        num += 1

print(pf)


