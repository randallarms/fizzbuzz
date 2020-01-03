#=====================================#
#             FizzBuzz                #
#          by Randall Arms            #
#  @ github.com/randallarms/fizzbuzz  #
#=====================================#

# Opening text
print("\n\n=========")
print("FIZZBUZZ!")
print("=========")

# Checks that the input n is a positive integer and returns an obj of int type
def int_check(n):
    try:
        return int(n)
    except ValueError:
        print("\nInput number must be a positive integer. ")
        exit()

# Input the maximum integer to iterate to
print("\nUp to which number would you like to iterate? ")
i = input("> ");

i_int = int_check(i)

# Check for large numbers and confirm
if int(i) > 1000:
    print("\nSet is greater than 1000 and may take a long time to finish. Type yes to confirm: ")
    confirm = input("> ");
    if confirm != "yes":
	    print("\nIteration canceled. ")
	    exit()

# Input "Fizz" divisor
print("\nWhich number would you like to check divisibility by for printing 'Fizz'? ")
f = input("> ");

f_int = int_check(f)

# Input "Buzz" divisor
print("\nWhich number would you like to check divisibility by for printing 'Buzz'? ")
b = input("> ");

b_int = int_check(b)

# Iterate through the integers and print results
print("\nIterating through each integer up to " + i + ": ")
for num in range(1, i_int+1):
	fizz = (num % f_int == 0)
	buzz = (num % b_int == 0)
	print('FizzBuzz' if (fizz & buzz) else 'Fizz' if fizz else 'Buzz' if buzz else num)