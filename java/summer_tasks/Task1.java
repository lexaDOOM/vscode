import java.util.Scanner;

public class Task1 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.print("Enter your username >> ");
        String username = input.nextLine();
        
        System.out.println("Hello, " + username + "!");
    }
}