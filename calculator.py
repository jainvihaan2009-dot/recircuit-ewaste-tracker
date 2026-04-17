def calculate_offset(weight_kg):
    # Average CO2 offset: 1kg of recycled e-waste saves ~1.5kg of CO2
    co2_saved = weight_kg * 1.5
    return co2_saved

print("--- RECIRCUIT E-Waste Impact Tracker ---")
weight = float(input("Enter e-waste collected (in kg): "))
print(f"Total CO2 prevented from entering atmosphere: {calculate_offset(weight)} kg")
