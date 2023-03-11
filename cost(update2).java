import java.util.Scanner;

public class FoodCostCalculator {
  public static void main(String[] args) {
    // Create a new Scanner object to read input from the user
    Scanner scanner = new Scanner(System.in);

    // Create a variable to store the total cost of all food items in KES
    int totalCost = 0;

    // Prompt the user for the budget in KES
    System.log("Enter the budget in KES: ");
    int budget = scanner.nextInt();

    // Loop until the user enters "done"
    while (true) {
      // Prompt the user for the name of the food item
      System.out.print("Enter the name of the food item (or 'done' to exit): ");
      String foodItem = scanner.nextLine();

      // If the user entered "done", exit the loop
      if (foodItem.equals("done")) {
        break;
      }

      // Prompt the user for the number of items
      System.out.print("Enter the number of items: ");
      int numItems = scanner.nextInt();

      // Prompt the user for the cost per item in KES
      System.out.print("Enter the cost per item in KES: ");
      int costPerItem = scanner.nextInt();

      // Calculate the total cost for this food item in KES
      int itemCost = numItems * costPerItem;

      // Add the total cost for this food item to the overall total cost in KES
      totalCost += itemCost;

      // Print the total cost for this food item in KES
      System.out.println("The total cost for " + numItems + " " + foodItem + " is KES " + itemCost);
    }

    // If the total cost is greater than the budget, calculate and print the recommended number of food items to purchase to stay within the budget
    if (totalCost > budget) {
      // Calculate the amount by which the total cost exceeds the budget
      int excessCost = totalCost - budget;

      // Calculate the recommended number of food items to purchase, rounded up to the nearest integer
      int numRecommendations = (int) Math.ceil(excessCost / 50.0);

      // Print the recommended number of food items to purchase
      System.out.println("To stay within the budget, purchase " + numRecommendations + " fewer food items whose cost is greater than KES 50.");
    }

    // Print the total cost for all food items in KES
    System.out.println("The total cost for all food items is KES " + totalCost);
  }
}
//This program is similar to the previous example, but it adds a step where it prompts the user for the budget in KES. If the total cost exceeds the budget, the program will calculate the number of food items to be purchased to keep the total cost within the