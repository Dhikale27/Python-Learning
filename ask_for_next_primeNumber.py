num = int(input("Enter a starting number: "))
ask = 'yes'
while ask == 'yes':
    for i in range(2,num):
        if num % i == 0:
            num += 1
          
            break

    else : 
       
        print(f"Next prime number is {num}")
    
        
        ask = input("do you wnat to go next: ")

        num +=1
