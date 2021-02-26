num = int(input("Enter a number: "))

for i in range(2,num +1):
    if i < num:
        if num % i == 0:
            print("it's not a prime number")
            break
        else:
            i += 1
    else:
        print("it's prime number")


