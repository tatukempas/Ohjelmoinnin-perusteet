print("Program starting.")
print("Testing decision structures.")

feed = int(input("Insert an integer: "))

print("Options:")
print("1 - In one multi-branched decision")
print("2 - In multiple independent if-statements")
print("0 - Exit")

choice = int(input("Your choice: "))

if choice == 1:
    print("Using one multi-branched decision structure.")
    if(feed >= 400):
        feed += 44
    elif(feed >= 200):
        feed += 22
    elif(feed >= 100):
        feed += 11
        print(f"Result is {feed}")
elif choice == 2:
    print("Using multiple idependent if-statements structure.")
    if(feed >= 400):
        feed += 44
    if(feed >= 200):
        feed += 22
    if(feed >= 100):
        feed += 11
        print(f"Result is {feed}")
elif choice == 0:
    print("Exiting...")
else:
    print("Unknown option.")

print("")
print("Program ending.")