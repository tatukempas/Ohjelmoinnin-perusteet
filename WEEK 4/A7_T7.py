print("Program starting.\n")

print("Check multiplicative persistence.")
n = int(input("Insert an integer: "))

steps = 0

while n >= 10:
    digits = [int(d) for d in str(n)]
    product = 1
    for d in digits:
        product *= d
    print(" * ".join(str(d) for d in digits), f"= {product}")
    n = product
    steps += 1

print("No more steps.\n")
print(f"This program took {steps} step(s)\n")

print("Program ending.")