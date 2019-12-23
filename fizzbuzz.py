print("Up to which number would you like to iterate through? ")
i = input();

if int(i) > 9999:
    print("This set has more than ten thousand iterations. Type yes to confirm: ")
    confirm = input();
    if confirm != "yes":
	    print("Iteration canceled. ")
    else:
        print("Iterating through each integer up to " + i + ": ")
		
        for fizzbuzz in range(int(i)):
            if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
                print("FizzBuzz")
                continue
            elif fizzbuzz % 3 == 0:
                print("Fizz")
                continue
            elif fizzbuzz % 5 == 0:
                print("Buzz")
                continue
            print(fizzbuzz)