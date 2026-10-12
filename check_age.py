try:

    age=int(input("Enter your age: "))

    if age%2 ==0:
        print("The age you inputted is even")
    else:
        print("The age you inputted is odd")
except ValueError:

    print("Value Error: Invalid input! Please enter a valid whole number")
finally:
    print("The file is shuttting down!")