def classify_number(num):
    if num < 0:
        print("The number is negative.")
    elif num == 0:
        print("The number is zero.")
    else:
        print("The number is positive.")

# Get user input
user_input = int(input("Enter a number: "))

# Call the function with user input
classify_number(user_input)
