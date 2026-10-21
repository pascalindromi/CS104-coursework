# Write a program that works out the cost of sending a parcel.

# 1. Ask for the weight in kg (decimals allowed), the destination (bangkok or other) and express (yes or no).
# 2. Up to 1 kg costs 40 baht, up to 5 kg 80 baht, up to 20 kg 150 baht.
# 3. Over 20 kg: print "Too heavy (max 20 kg)".
# 4. Destination other: add 30 baht (store it in a constant, e.g. OUTSIDE_FEE = 30).
# 5. Express: double the price (after adding the destination fee).
# 6. Weight that is not a number, or 0 and below: print "Please enter a valid weight" (use try/except).
# 7. Any other destination: print "Unknown destination".

# Example:
# Weight (kg): 3
# Destination (bangkok/other): other
# Express? (yes/no): yes
# Shipping cost: 220 baht

# Test your program with all of these:
# 3, bangkok, no → Shipping cost: 80 baht
# 3, other, yes → Shipping cost: 220 baht
# 1, other, no → Shipping cost: 70 baht
# 20, bangkok, yes → Shipping cost: 300 baht
# 0.5, bangkok, yes → Shipping cost: 80 baht
# 25 → Too heavy (max 20 kg)
# abc → Please enter a valid weight
# 0 → Please enter a valid weight
# 2, chiang mai → Unknown destination

# Submit: create a new GitHub repository called hw03, push parcel_shipping.py to it, and submit the repository link here.

try: 
    weight = float(input("Weight (in kg): "))
    if weight < 0: raise ValueError("Weight cannot be negative")
except ValueError:
    print("Please enter a valid weight")
    exit()

destination = input("Destination (bangkok/other): ")
express = input("Express? (yes/no): ")
if weight <= 0:
    print("Please enter a valid weight")
if weight > 20:
    print("Too heavy (max 20 kg)")
if weight <= 1:
    cost = 40
if weight > 1 and weight <= 5:
    cost = 80
if weight > 5 and weight <= 20:
    cost = 150

OUTSIDE_FEE = 30
if destination == "other":
    cost += OUTSIDE_FEE
if express == "yes":
    cost *= 2
if destination != "bangkok" and destination != "other":
    print("Unknown destination")

print(f"Shipping cost: {cost} baht")