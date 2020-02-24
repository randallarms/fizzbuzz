/*===================================*\
#           FizzBuzz (C#)             #
#          by Randall Arms            #
#  @ github.com/randallarms/fizzbuzz  #
\*===================================*/

using System;
using System.Linq;

namespace FizzBuzz
{
	class FizzBuzzEval
	{
		
		// Checks that the input n is a positive integer and returns an obj of int type
		static int int_check(string n)
		{
			int i;
			if (int.TryParse(n, out i) && i > 0)
			{
				return i;
			}
			else
			{
				Console.WriteLine("\nInput number must be a positive integer. ");
			}
			return -1;
		}
		
		static void Main()
		{

			// Opening text
			Console.WriteLine("\n\n=========");
			Console.WriteLine("FIZZBUZZ!");
			Console.WriteLine("=========");

			// Input the maximum integer to iterate to
			Console.WriteLine("\nUp to which number would you like to iterate? \n> ");
			string i = Console.ReadLine();

			int i_int = int_check(i);
			if (i_int < 0) {
				return;
			}

			// Check for large numbers and confirm
			if (i_int > 1000)
			{
				Console.WriteLine("\nSet is greater than 1000 and may take a long time to finish. Type yes to confirm: \n> ");
				string confirm = Console.ReadLine();
				if (confirm != "yes")
				{
					Console.WriteLine("\nIteration canceled. ");
					return;
				}
			}

			// Input "Fizz" divisor
			Console.WriteLine("\nWhich number would you like to check divisibility by for printing 'Fizz'? \n> ");
			string f = Console.ReadLine();

			int f_int = int_check(f);
			if (f_int < 0) {
				return;
			}

			// Input "Buzz" divisor
			Console.WriteLine("\nWhich number would you like to check divisibility by for printing 'Buzz'? \n> ");
			string b = Console.ReadLine();

			int b_int = int_check(b);
			if (b_int < 0) {
				return;
			}

			// Iterate through the integers and print results
			Console.WriteLine("\nIterating through each integer up to " + i + ": ");
			foreach (int num in Enumerable.Range(1, i_int))
			{
				bool fizz = (num % f_int == 0);
				bool buzz = (num % b_int == 0);
				Console.WriteLine((fizz && buzz) ? "FizzBuzz" : fizz ? "Fizz" : buzz ? "Buzz" : num.ToString());
			}
				
		}
	}
}