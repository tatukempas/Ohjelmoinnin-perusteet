print("Calculate fuel consumption.")
Feed = input("Enter travel distance(kilometers): ")
Distance = int(Feed)
Feed = input("Enter fuel usage(liters): ")
FuelUsage = int(Feed)
Consumption = Distance / FuelUsage
Consumption = int(Consumption)
print("Fuel consumption is", Consumption, "l per 100km")
