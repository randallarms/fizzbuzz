print("=========")
print("FIZZBUZZ!")
print("=========")

print("Up to which number would you like to iterate? ")
i = input("> ");

if int(i) > 999:
    print("This set has a thousand or more iterations and may take a very long time to finish. Type yes to confirm: ")
    confirm = input("> ");
    if confirm != "yes":
	    print("Iteration canceled. ")
	    exit()

print("Iterating through each integer up to " + i + ": ")
for num in range(1, int(i)+1):
	fizz = (num % 3 == 0)
	buzz = (num % 5 == 0)
	print('FizzBuzz' if (fizz & buzz) else 'Fizz' if fizz else 'Buzz' if buzz else num)