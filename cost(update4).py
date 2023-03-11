# In this updated code, the calculate_total_cost() function keeps track of the excess costs of each item in the list (i.e., the costs of items that exceed KES 50). If the total cost exceeds the maximum cost, the function calculates the maximum number of items that can be purchased for each item in the excess costs list to stay within the maximum cost. It then returns an error message along with a list of recommended items and their maximum number of items. Otherwise, it returns the formatted total cost and currency code as before.
import math


def calculate_total_cost(items, currency_code, max_cost):
    total_cost = 0
    excess_costs = []
    for item in items:
        food_type, number_of_items, cost_per_item = item
        item_cost = number_of_items * cost_per_item
        total_cost += item_cost
        if item_cost > 50:
            excess_costs.append((food_type, item_cost))

    if total_cost > max_cost:
        # calculate the maximum number of items that can be purchased for each item in excess_costs
        recommended_items = []
        remaining_cost = max_cost
        for food_type, item_cost in excess_costs:
            max_number_of_items = math.floor(remaining_cost // cost_per_item)
            if max_number_of_items < 1:
                max_number_of_items = 1
            recommended_items.append((food_type, max_number_of_items))
            remaining_cost -= max_number_of_items * cost_per_item

        print("Warning: Total cost exceeds the maximum cost. Recommended items: " +
              str(recommended_items))
    return format(total_cost, ".2f") + " " + currency_code


def get_food_list():
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
    return food_list


def get_max_cost():
    max_cost = input("Enter the maximum cost: ")
    try:
        max_cost = float(max_cost)
    except ValueError:
        print("Invalid input. Please enter a valid number.")
    return max_cost


def print_total_cost(total_cost):
    print("The total cost of your purchase is: " + total_cost)


# get input from the user
food_list = get_food_list()

# get the maximum cost from the user
max_cost = get_max_cost()

# calculate the total cost
total_cost = calculate_total_cost(food_list, "KES", max_cost)

# print the result
print_total_cost(total_cost)
