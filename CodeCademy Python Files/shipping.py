# control flow exercise from Codecademy, including If, elif, else statements, boolean and logical operators
# a program that computes the shipping cost based on the weight of the package
weight = 41.5


#Ground shipping
if weight <= 2:
  cost_ground= weight * 1.5 + 20
elif weight <= 6:
  cost_ground= weight * 3.0 +20
elif weight <= 10 :
  cost_ground= weight * 4.0 +20
else:
  cost_ground= weight * 4.75 +20
print("Ground Shipping:")
print(weight, "lbs")
print("Cost: $" + str(cost_ground))

#premium ground shipping
ground_shipping_premium = 125
print("Ground Shipping Premium:$",
ground_shipping_premium)

#drone shipping
if weight <= 2:
  cost_drone= weight * 4.50
elif weight <= 6:
  cost_drone= weight * 9.0
elif weight <= 10 :
  cost_drone= weight * 12.0
else:
  cost_drone= weight * 14.25

print("Drone Shipping:")
print(weight, "lbs")
print("Cost: $" + str(cost_drone))