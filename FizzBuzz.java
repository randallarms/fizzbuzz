/*===================================*\
#          FizzBuzz (Java)            #
#          by Randall Arms            #
#  @ github.com/randallarms/fizzbuzz  #
\*===================================*/

import java.util.Scanner;
import java.util.stream.IntStream;

public class FizzBuzz {
	
	// Checks that the input n is a positive integer and returns an obj of int type
	static int int_check(String n) {
		
		int c_int = 0;
		
		try {
			c_int = Integer.parseInt(n);
		} catch(NumberFormatException e) {
			System.out.println("\nInput number must be an integer. ");
			System.exit(0);
		}
		
		if (c_int >= 0) {
			return c_int;
		} else {
			System.out.println("\nInput number must be a positive integer. ");
			System.exit(0);
			return 0;
		}
		
	}
	
	// Main method
	public static void main(String[] args) {

		// Opening text
		System.out.println("\n\n=========");
		System.out.println("FIZZBUZZ!");
		System.out.println("=========");
		
		// Scanner obj
		Scanner scanner = new Scanner(System.in);

		// Input the maximum integer to iterate to
		System.out.println("\nUp to which number would you like to iterate? ");
		String i = scanner.nextLine();

		int i_int = int_check(i);

		// Check for large numbers and confirm
		if (i_int > 1000) {
			System.out.println("\nSet is greater than 1000 and may take a long time to finish. Enter 'yes' to confirm: ");
			String confirm = scanner.nextLine();
			if (!confirm.contains("yes")) {
				System.out.println("\nIteration canceled. ");
				System.exit(0);
			}
		}

		// Input "Fizz" divisor
		System.out.println("\nWhich number would you like to check divisibility by for printing 'Fizz'? ");
		String f = scanner.nextLine();

		int f_int = int_check(f);

		// Input "Buzz" divisor
		System.out.println("\nWhich number would you like to check divisibility by for printing 'Buzz'? ");
		String b = scanner.nextLine();

		int b_int = int_check(b);

		// Iterate through the integers and print results
		System.out.println("\nIterating through each integer up to " + i + ": ");
		IntStream range = IntStream.range(1, i_int+1);
		for (int num : range.toArray()) {
			boolean fizz = (num % f_int == 0);
			boolean buzz = (num % b_int == 0);
			System.out.println((fizz && buzz) ? "FizzBuzz" : fizz ? "Fizz" : buzz ? "Buzz" : Integer.toString(num));
		}
			
	}
	
}