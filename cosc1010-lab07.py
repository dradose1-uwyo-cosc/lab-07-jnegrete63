# Your Name Here: Jose Fabian Negrete Oseguera
# UWYO COSC 1010
# Submission Date: 10/29/2024
# Lab 09
# Lab Section: 11
# Sources, people worked with, help given to: I got help from my TA'S and help from microsoft AI co-pilot
# your
# comments
# here :I cant figure out how to make it work, i tryed serching on google and using AI to help me but i was not able to get much out of it. for part 3


# Prompt the user for an upper bound 
# Write a while loop that gives the factorial of that upper bound
# This will need to be a positive number
# For this you will need to check to ensure that the user entered a number
    # To do so you can use the methods `.isdigit()` or `.isnumeric()`
    # If a user did not enter a number output a statement saying so
# You will continue to prompt the user until a proper integer value is entered


while True:
    prompt = input("Type a positive number that will become the upper bound:  ")
    if input == "exit":
        break
    if prompt.isdigit():
        prompt = (int(prompt))
       
    else:
        print(f"Sorry that is not an acceptible upper bound, pleas try again {prompt}")
    break

factorial = 1

i = 1

while i <= prompt:
    factorial *= i
    i += 1

print(f"The result of the factorial based on the given bound is {factorial}")

print("*"*75)
# Create a while loop that prompts a user for input of an integer values
# Sum all inputs. When the user enters 'exit' (regardless of casing) end the loop
# Upon ending the loop print the sum
# Your program should accept both positive and negative input
# Remember all inputs from stdin are strings, so you will need to convert the string to an int first
# Before you convert the number you need to check to ensure that it is a numeric string
    # To do so you can use the methods `.isdigit()` or `.isnumeric()`
    # This will return true if every digit in your string is a numerical character
    # However, that means a string such as `-1` would return false, even though your program should accept negative values
    # This means you will need to have a check to see if `-` is first character of the string before you check if it is numerical
    # If it is in the string you will need to remove the `-` character, and know that it will be a negative number, so a subtraction from the overall sum
    # I recommend checking out: https://www.w3schools.com/python/ref_string_replace.asp to figure out how one may remove a character from a string
# All this together means you will have an intensive while loop that includes multiple if statements, likely with some nesting 
# The sum should start at 0 

num_sum = 0 

while True:
    num_input = input("Enter a numeric value, or type exit to add values together:  ")
    if num_input.isdigit():
        num_sum += int(num_input)
    elif num_input[0] == "-" and num_input [1:].isdigit():
        num_sum -= int(num_input[1:])
    elif num_input:
        num_input.lower() == "exit"
        break
    else:
        print("sorry that is not an acceptible answer, try again")

    

print(f"Your final sum is {num_sum}")

print("*"*75)
# Now you will be creating a two operand calculator
# It will support the following operators: +,-,/,*,% 
# So accepted input is of the form `operand operator operand` 
# You can assume that the user is competent and will only input strings of that form 
# You will again need to verify that the operands are numerical values
# For this assume only positive integers will be entered, no need look for negative numbers 
# You will need to check the string for which operator it contains
# Once you do, you will need to remove the operands from the string
# This can be done in multiple ways:
    # You can go through the string in a loop and create a substring of the characters until an operator is reached
        # Upon reaching the operator you will switch to another substring and add all characters following to the second new string 
    # Alternatively you can use the `.split()` method to split the string around an operator: https://www.w3schools.com/python/ref_string_split.asp
# Your program will need to work with whatever spacing is given  
    # So, it should function the same for `5 + 6` as `5+6`
# Print the result of the equation
# Again, loop through prompting the user for input until `exit` in any casing is input 


        #I cant figure out how to make it work, i tryed serching on google and using AI to help me but i was not able to get much out of it. 
while True:
    user_input = input("Enter a sequense such as 1+1, 3-2, 3*2, 4/2, 2%4 using positive numbers:  ")
    
    if user_input.lower() == "exit":
        break

    operators = ["+", "-", "*", "/", "%"]

    for operator in operators:
        if operator in user_input:
            numbers = user_input.split(operator)
            numbers = int(user_input[0].isdigit)
            numbers = int(user_input[1].isdigit)

            final_output = 0
            match operator:
                case "+":
                    final_output = numbers[0] + numbers[1]
                case "-":
                    final_output = numbers[0] - numbers[1]
                case "*":
                    final_output = numbers[0] * numbers[1]
                case "/":
                    final_output = numbers[0] / numbers[1]
                case "%":
                    final_output = numbers[0] % numbers[1]

print(f"you enterd {user_input}, and your result is {final_output}")




#if user_input.isdigit():
        #user_input = int(user_input)
    #elif num_input[0] == "-" and num_input [1:].isdigit():
        #num_sum = int(user_input)
    #else:
        #print("Sorry that is not an acceptible form of input")
        #continue
