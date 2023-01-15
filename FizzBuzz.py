n=int(input("Enter Number:\n"))
print("\n")
for x in range(1,n,2):
    if x % 3==0 and x % 5==0:
        print("FizzBuzz")
        continue
    elif x % 3 == 0:
        print("Fizz")
        continue
    elif x % 5 == 0:
        print("Buzz")
        continue
    else:
        print(x)
# input:15
#1
#Fizz
#Buzz
#7
#Fizz
#Buzz
#11
#13

#explanation
#all number rounded by 2 will not be printed
#all number rounded by 3 will be printed by Fizz
#all number rounded by 5 will be printed by Buzz
#if number rounded by 3 and 5 will be printed by FizzBuzz
#the last number input will be break
