print("Up to which number would you like to iterate? ")
i = input();

if int(i) > 9999:
    print("This set has more than ten thousand iterations and may take a very long time to finish. Type yes to confirm: ")
    confirm = input();
    if confirm != "yes":
	    print("Iteration canceled. ")
	    exit()

print("Iterating through each integer up to " + i + ": ")

for fizzbuzz in range(1, int(i)+1):
	output = ""

	if fizzbuzz % 3 == 0:
		output += "Fizz"
	if fizzbuzz % 5 == 0:
		output += "Buzz"

	print(output or fizzbuzz)