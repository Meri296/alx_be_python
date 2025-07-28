# pattern_drawing.py

# Prompt the user for the pattern size
size = int(input("Enter the size of the pattern: "))

# Validate input
if size <= 0:
    print("Please enter a positive integer.")
else:
    row = 0  # Initialize row counter
    while row < size:
        # For each row, print 'size' number of asterisks
        for col in range(size):
            print("*", end="")
        print()  # Move to the next line
        row += 1
