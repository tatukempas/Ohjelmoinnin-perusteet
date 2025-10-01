# print("Welcome to the app!")
# Temp = int(input("What is the temperature of CPU?"))
# if(Temp > 80):
#     print("Warning! CPU temperature too high!")
# else:
#     print("All cool, keep on going!")


# print("Prgoram starting.")
# num = int(input("Insert a number: "))
# if(num % 2 == 0):
#    print(f"{num} is even")
# else:
#    print(f"{num} is odd")
# print("Program ending.")

# if Temp > 90:
#     print("You are toast")
# elif Temp > 80:
#     print("Warning")
# else:
#     print("You are ok")


# town = "Lahti"
# street = "Mukkulankatu"
# building = 19

# if(town == "Lahti" and street == "Mukkulankatu" and building == 19):
#     print("You are at LAB")
# elif(town == "Lahti" and (street != "Mukkulankatu" or building != 19)):
#     print("You are in correct town, but check the street address again")
# elif not(town == "Lahti" and street == "Mukkulankatu" and building == 19):
#     print("You are completely lost...)")

import random

print(random.randint(1, 6))

vaihtoehdot = ["kivi", "paperi", "sakset"]
pelaaja = str(input("Valitse kivi, paperi tai sakset: "))
tietokone = random.choice(vaihtoehdot)
print(f"Tietokone valitsi: {tietokone}")


