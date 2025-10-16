# Input variables (you can change these to test different scenarios)
weight = 25  # in pounds
destination = "international"  # "domestic" or "international"
membership = "premium"  # "standard" or "premium"

# Start calculating
base_cost = 10
shipping_cost = base_cost
details = [f"Base ${base_cost}"]

# Overweight check
if weight > 20:
    shipping_cost += 5
    details.append("Overweight $5")

# International check
if destination == "international":
    if membership != "premium":
        shipping_cost *= 2
        details.append("International surcharge: cost doubled")
    else:
        details.append("International fee waived")

# Premium member discount
if membership == "premium":
    discount = 0.20 * shipping_cost
    shipping_cost *= 0.80
    details.append("Premium 20% discount applied")

# Final output
print(f"Weight (lbs): {weight}")
print(f"Destination (domestic/international): {destination}")
print(f"Membership (standard/premium): {membership}")
print(f"Final Shipping Cost: ${shipping_cost:.2f}")
print(f"(Details: {', '.join(details)}.)")
