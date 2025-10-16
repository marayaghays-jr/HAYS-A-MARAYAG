 
age = int(input("Enter your age: "))
is_student_input = input("Are you a student? (True/False): ")

is_student = is_student_input.strip().lower() == "true"

# 2. Base ticket price
base_price = 12

 #DETERMAIN THE DISCOUNT
if age <= 12:
    discount = 3   
elif age >= 65:
    discount = 4   
elif is_student:
    discount = 2   
else:
    discount = 0   

# 4. Calculate final price
final_price = base_price - discount

# 5. Output result
print(f"\nAge: {age}")
print(f"Is student? {is_student}")
print(f"Your ticket price is ${final_price}.")
