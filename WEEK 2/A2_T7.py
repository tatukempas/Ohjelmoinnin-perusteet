print("Program starting.")
fah = float(input("Insert fahrenheits: "))
cel = (fah -32) / 1.8
cel = round(cel, 1)
print(f"{fah}°F is {cel}°C")
print("Program ending.")