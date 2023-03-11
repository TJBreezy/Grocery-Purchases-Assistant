# ad multiple food at time
def calculate_total_cost(food_list):
    total_cost = 0
    for food in food_list:
        food_type, number_of_items, cost_per_item = food
        total_cost += number_of_items * cost_per_item
    return total_cost


# get input from the user
food_list = []
for i in range(20):
    food_type = input("Enter the type of food (" + str(i + 1) + " of 20): ")
    number_of_items = input("Enter the number of items: ")
    cost_per_item = input("Enter the cost per item: ")
    try:
        number_of_items = float(number_of_items)
        cost_per_item = float(cost_per_item)
    except ValueError:
        print("Invalid input. Please enter valid numbers.")
    food_list.append((food_type, number_of_items, cost_per_item))

# calculate the total cost
total_cost = calculate_total_cost(food_list)

# print the result
print("The total cost of your purchase is: $" + str(total_cost))
