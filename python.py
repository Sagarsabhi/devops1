def calculate_electricity_bill(previous_charges, units_consumed):
    # Define slab rates as per government scheme
    if units_consumed <= 50:
        current_charges = units_consumed * 2.60
        surcharge = 25
    elif units_consumed <= 100:
        current_charges = 130 + ((units_consumed - 50) * 3.25)
        surcharge = 35
    elif units_consumed <= 200:
        current_charges = 130 + 162.50 + ((units_consumed - 100) * 5.26)
        surcharge = 45
    else:
        current_charges = 130 + 162.50 + 526 + ((units_consumed - 200) * 8.45)
        surcharge = 75

    # Calculate total bill
    total_bill = previous_charges + current_charges + surcharge
    return total_bill

# Example usage
previous_charges = float(input("Enter previous charges: "))
units_consumed = int(input("Enter the number of units consumed: "))
total_bill = calculate_electricity_bill(previous_charges, units_consumed)
print(f"Total Electricity Bill: ₹{total_bill:.2f}")
