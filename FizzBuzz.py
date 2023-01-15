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