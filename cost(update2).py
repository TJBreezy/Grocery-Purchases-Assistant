# ability to use kes and add the specific amount of food
def calculate_total_cost(food_list, currency):
    total_cost = 0
    for food in food_list:
        food_type, number_of_items, cost_per_item = food
        total_cost += number_of_items * cost_per_item
    return format(total_cost, ".2f") + " " + currency


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

# calculate the total cost
total_cost = calculate_total_cost(food_list, "KES")

# print the result
print("The total cost of your purchase is: " + total_cost)
