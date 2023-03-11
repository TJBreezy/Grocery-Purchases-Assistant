import java.util.Scanner;

public class FoodCostCalculator {
  public static void main(String[] args) {
    // Create a new Scanner object to read input from the user
    Scanner scanner = new Scanner(System.in);

    // Create a variable to store the total cost of all food items in KES
    int totalCost = 0;

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

    // Print the total cost for all food items in KES
    System.out.println("The total cost for all food items is KES " + totalCost);
  }
}

//This program is similar to the previous example, but it uses Kenyan shillings (KES) as the currency and it uses int variables to store the cost per item and the total cost, since KES is a whole number currency. The program prompts the user for the cost per item in KES and calculates the total cost in KES, and it prints the total cost in KES.