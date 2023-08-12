# Review: 
# Create a function called greet(). 
# Write 3 print statements inside the function.
# Call the greet() function and run your code.

def greet():
	print('Hello')
	print('Good to see you')
	print("Let's Begin")

greet()


def greet_with_name(name):
	print(f'Hello {name}')
	print('Good to see you')
	print(f"Let's Begin {name}")	


greet_with_name(input('Please enter your name '))