#why is is coming down on another line. :)

def property_tax():
	value =float(input("Enter the actual value: "))
	assessed_value = 0.6 * value
	print("Assesed Value: " + str(assessed_value))
	tax = .72 * assessed_value

	value = format(value, ",.2f")

	print("Property tax: " + str(round(tax, 2)))

property_tax()

#5.9 HW
def future_value():
	#get present value, 
	present_value = float(input("Enter the present value of the account in dollars: "))
	#get i 
	interest_rate = float(input("Enter the monthly interest rate as a percentage: "))

	#get months or time 
	time = float(input("Enter the number of months: "))
	print("The information for your account is: ")

	print("Present Value: $" + format(present_value, ".2f"))
	print("Interest rate: %" + format(interest_rate, ".2f"))



	P = present_value 
	i = interest_rate / 100
	t = time

	F = P * (1 + i)**t
	print("After 12 months, the value of your account will be $" + format(F, ".2f"))



future_value()




#7.8HW3.py :)
#generation z search 

def genz_search():

	boy_list = open("BoyNames.txt", "r")
	girl_list = open("GirlNames.txt", "r")
	popular_boys = boy_list.readlines()
	popular_girls = girl_list.readlines()

	for i in range(len(popular_boys)):
		popular_boys[i] = popular_boys[i].rstrip("\n")


	for i in range(len(popular_girls)):
		popular_girls[i] = popular_girls[i].rstrip("\n")

	b_output = ""
	g_output = ""


	boy_name = input("Enter a boy's name, or N if you do nto wish to enter a boy's name: ")
	girl_name = input("Enter a girl's name, or N if tou do not wish to enter a girl's name: ")

	for i in range(len(popular_boys)):
		if(boy_name) == ("N"):
			b_output = boy_name + "You chose not to enter a boys name."
			break
		elif(boy_name == popular_boys[i]):
			b_output = boy_name + "is one of the most popular boy's names."
			break 
		elif(boy_name != popular_boys[i]):
			b_output = boy_name + "is not one of the most popular boy's names."

	for i in range(len(popular_girls)):
		if(girl_name) == ("N"):
			g_output = girl_name + "You chose not to enter a girl's name."
		elif(girl_name == popular_girls[i]):
			g_output = girl_name + "is one of the most popular girl's names"
			break
		elif(girl_name != popular_girls[i]):
			g_output = girl_name + "is not one of the most popular girl's names"






	print(b_output)
	print(g_output)


genz_search()



#7.12HW3.py :) 
def prime_gen():

	user_integer = input("Enter an interger greater than 1: ")


	for i in range(2, int(user_integer) + 1):
		num = 0
		for j in range(2,i):


				if (i % j == 0):
					num = 1
		if (num == 0):
			print(i, "is prime")

		elif(num == 1):
			print(i, "is composite")


			
prime_gen()


#9.10HW2 Jean Tirole Nobel Index


# The get_word_dict function returns a dictionary containing
# the words from line_list as keys, and their line numbers
# as values.
def get_word_dict(line_list):


    # Create a dictionary to hold the words.
	word_dict = {}

    # Step through the list of lines.
	for e in line_list:
        # Split the line into words.
		words = e.split(' ')
        # Step through the list of words.
		for w in words:
            # If the word is in the dictionary...

			if w in word_dict:
                # Update the existing value.
				word_dict[w] += 1
                #YOUR CODE HERE
                #find key, and assign line number as value 
                #  Find w in the dictionary, add the new line number to that key value
                # word_dict[w] = word_dict[w] + e
			else:
				word_dict[w] = 1 
                # Otherwise, store the word in the dictionary. set the count to 1. 
                #YOUR CODE HERE
	print(word_dict)
	sortedlist = sorted(word_dict)
    # Return the dictionary.
	return(word_dict)

# The write_index_file function writes an index file containing the
# elements of the word_dict dictionary.
def write_index_file(word_dict):
    # Open the file.
	outputfile = open('index_j.txt', 'w')

    # Write the entries from the dictionary.
	sortedlist = sorted(word_dict)
	for key in sortedlist:
        # Write the word to the dictionary
		outputfile.write(key + ":" + str(word_dict[key]))#YOUR CODE IN HERE))
		outputfile.write('\n') #this writes a space to the line



    # Close the file.
	outputfile.close()
    
def main():
    # Open the file.
	inputfile = open('tirole_nobel.txt', 'r')

    # Read the file's contents into a list.
	line_list = inputfile.readlines()

    # Close the file.
	inputfile.close()

    # Strip the newline from each list element.
	for i in range(len(line_list)):
		line_list[i] = line_list[i].rstrip('\n')


    # Get a dictionary holding the words and their line numbers.
	word_dict = get_word_dict(line_list)

    # Write the index file.
	write_index_file(word_dict)

main()


def power_recursive():
	base = float(input("Enter a number: "))
	power = float(input("Enter a positive whole number between 1 and 100: "))
	#this next line calls the code from the recursion base power part 
	answer = recursion(base, power)
	base = format(float(base), ".2f")
	#expo = format(float(base) ** float(power), ",.2f")
	print(str(base) + " raised to the power of " + str(power) + " is " + str(answer))
def recursion(base,power):
	# you always need a base case for recursive approach
	if power == 0:
		return 1
	else:
		return(base * recursion(base,power -1)) 
		#recursion(base,power) returns a number, so it is a number itself
power_recursive()
