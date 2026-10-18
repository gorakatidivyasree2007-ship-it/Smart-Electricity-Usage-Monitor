appliances = {
    "Fan": (75, 8),
    "TV": (100, 4),
    "Lights": (60, 6),
    "Refrigerator": (200, 10)
}

rate = float(input("Electricity rate per kWh (Rs): "))
total = 0

for name, (watts, hours) in appliances.items():
    energy = watts * hours / 1000
    total += energy
    print(name, ":", round(energy, 2), "kWh/day")

print("Daily consumption:", round(total, 2), "kWh")
print("Monthly bill: Rs", round(total * 30 * rate, 2))
