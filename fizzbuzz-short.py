for n in range(1, 101):
	f = (n % 3 == 0)
	b = (n % 5 == 0)
	print('FizzBuzz' if (f&b) else 'Fizz' if f else 'Buzz' if b else n)