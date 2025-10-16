 
inches_input = input("Enter the number of inches: ")

# Convert the input to an integer
total_inches = int(inches_input)

# Calculate feet and remaining inches
feet = total_inches // 12
remaining_inches = total_inches % 12

# Print the result
print(f"{total_inches} inches is equal to {feet} feet and {remaining_inches} inches.")

