class FizzBuzz
{
	static void Main()
	{
		foreach(int n in System.Linq.Enumerable.Range(1, 100))
		{
			bool f = (n % 3 == 0);
			bool b = (n % 5 == 0);
			System.Console.WriteLine((f&&b) ? "FizzBuzz" : f ? "Fizz" : b ? "Buzz" : n.ToString());
		}
	}
}