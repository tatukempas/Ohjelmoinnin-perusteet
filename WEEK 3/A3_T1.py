print("Program starting.")
print("Print insert two integers")
num1 = int(input("Insert first integer: "))
num2 = int(input("Insert second integer: "))
print("Comapring inserted integers...")
if(num1 > num2):
    print("First integer is greater.")
elif(num1 < num2):
    print("Second integer is greater.")
else:
    print("Integers are the same.")

print("Adding integers together...")
sum = num1 + num2
print(f"{num1} + {num2} = {sum}")

print("Checking the parity of the sum...")
if(sum % 2 == 0):
    print("The sum is even")
else:
    print("The sum is odd")
print("Program ending.")