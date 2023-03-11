# input maximum total cost
def calculate_total_cost(items, currency_code, max_cost):
    total_cost = 0
    for item in items:
        food_type, number_of_items, cost_per_item = item
        total_cost += number_of_items * cost_per_item

    if total_cost > max_cost:
        return "Error: Total cost exceeds the maximum cost."
    else:
        return format(total_cost, ".2f") + " " + currency_code


# get input from the user
food_list = []
while True:
    food_type = input("Enter the type of food: ")
    if food_type == "":
        # an empty food_type indicates that the user is done entering items
        break
    number_of_items = input("Enter the number of items: ")
    cost_per_item = input("Enter the cost per item: ")
    try:
        number_of_items = float(number_of_items)
        cost_per_item = float(cost_per_item)
    except ValueError:
        print("Invalid input. Please enter valid numbers.")
    food_list.append((food_type, number_of_items, cost_per_item))

# get the maximum cost from the user
max_cost = input("Enter the maximum cost: ")
try:
    max_cost = float(max_cost)
except ValueError:
    print("Invalid input. Please enter a valid number.")

# calculate the total cost
total_cost = calculate_total_cost(food_list, "KES", max_cost)

# print the result
print("The total cost of your purchase is: " + total_cost)
