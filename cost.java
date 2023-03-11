//calculates total cost for one item
import java.util.Scanner;

public class FoodCostCalculator {
  public static void main(String[] args) {
    // Create a new Scanner object to read input from the user
    Scanner scanner = new Scanner(System.in);

    // Prompt the user for the name of the food item
    System.out.print("Enter the name of the food item: ");
    String foodItem = scanner.nextLine();

    // Prompt the user for the number of items
    System.out.print("Enter the number of items: ");
    int numItems = scanner.nextInt();

    // Prompt the user for the cost per item
    System.out.print("Enter the cost per item: ");
    double costPerItem = scanner.nextDouble();

    // Calculate the total cost
    double totalCost = numItems * costPerItem;

    // Print the total cost
    System.out.println("The total cost for " + numItems + " " + foodItem + " is $" + totalCost);
  }
}
import java.util.Scanner;

public class FoodCostCalculator {
  public static void main(String[] args) {
    // Create a new Scanner object to read input from the user
    Scanner scanner = new Scanner(System.in);

    // Prompt the user for the name of the food item
    System.out.print("Enter the name of the food item: ");
    String foodItem = scanner.nextLine();

    // Prompt the user for the number of items
    System.out.print("Enter the number of items: ");
    int numItems = scanner.nextInt();

    // Prompt the user for the cost per item
    System.out.print("Enter the cost per item: ");
    double costPerItem = scanner.nextDouble();

    // Calculate the total cost
    double totalCost = numItems * costPerItem;

    // Print the total cost
    System.out.println("The total cost for " + numItems + " " + foodItem + " is $" + totalCost);
  }
}
