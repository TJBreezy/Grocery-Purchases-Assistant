# define a function that calculates the total cost of a purchase
def calculate_total_cost(food_type, number_of_items, cost_per_item):
    total_cost = number_of_items * cost_per_item
    return total_cost


# get input from the user
food_type = input("Enter the type of food: ")
number_of_items = input("Enter the number of items: ")
cost_per_item = input("Enter the cost per item: ")

# convert the inputs to numbers (floats)
try:
    number_of_items = float(number_of_items)
    cost_per_item = float(cost_per_item)
except ValueError:
    print("Invalid input. Please enter valid numbers.")

# calculate the total cost
total_cost = calculate_total_cost(food_type, number_of_items, cost_per_item)

# print the result
print("The total cost of your purchase is: $" + str(total_cost))
