###################################
#Task A9_T4
#Developer Tatu Kempas
#2.12.2025
###################################

TEMP_MIN = -273.15
TEMP_MAX = 10000

def collectCelsius():
    feed = input("Insert Celsius: ")
    try:
        c = float(feed)
    except ValueError:
        raise ValueError("could not convert string to float: '{}'".format(feed))

    if c < TEMP_MIN or c > TEMP_MAX:
        raise Exception("{} temperature out of range.".format(c))

    return c


print("Program starting.")

try:
    celsius = collectCelsius()
    print("You inserted {} °C".format(celsius))
except Exception as e:
    print(e)

print("Program ending.")
