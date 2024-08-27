package edu.penzgtu;
import java.util.Scanner;
import edu.Sort;

/**
 * Hello world!
 *
 */
public class App 
{

    public static void printArray(int[] array) {
        for (int i : array) {
            System.out.print(i + " ");
        }
        System.out.println();
    }

    public static void main( String[] args ) {
        Scanner input = new Scanner(System.in);
        System.out.print("Enter array length >> ");
        int len = input.nextInt();
        int[] array = new int[len];

        for (int i = 0; i < len; i++) {
            System.out.print("Enter " + (i + 1) + " number >> ");
            array[i] = input.nextInt();
        }

        System.out.println("Original array: ");
        printArray(array);

        Sort.shellSort(array);

        System.out.println("Sorted Array: ");
        printArray(array);
    }
    }
