# Python Pizza Deliveries
# A simple script to calculate the total cost of a pizza order based on the user inputs.

print("Welcome to Python pizza deliveries👌!")

# Function to get valid inputs for pizza size
def get_pizza_size():
    while True:
        size = input("What pizza size do you want? S, M, L: ").lower()
        if size in ["s", "m", "l"]:
            return size
        else:
            print("You entered wrong inputs for size. Try again.")

# Function to get valid inputs for pepperoni
def get_pepperoni_choice ():
    while True:
        pepperoni = input("Do you want pepperoni on your pizza? Y or N: ").lower()
        if pepperoni in ["y", "n"]:
            return pepperoni
        else:
            print("You entered the wrong inputs for pepperoni. Please try again")

# Function to get valid inputs for pepperoni
def get_extra_cheese_choice ():
    while True:
        extra_cheese = input("Do you want extra cheese on your pizza? Y or N: ").lower()
        if extra_cheese in ["y", "n"]:
            return extra_cheese
        else:
            print("You entered wrong inputs for extra cheese.Please try again")

# Get user inputs with validations
size = get_pizza_size()
pepperoni = get_pepperoni_choice()
extra_cheese = get_extra_cheese_choice()

# Calculate the cost of the pizza
bill = 0
if size == "s":
    bill += 15
elif size == "m":
    bill += 20
elif size == "l":
    bill += 25

# Add cost for pepperoni
if pepperoni == "y":
    if size == "s":
        bill += 2
    else:
        bill += 3

# Add cost for extra cheese
if extra_cheese == "y":
    bill += 1

# Output final bill
print(f"\nYour Final bill is ${bill}")