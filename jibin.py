def print_multiplication_table(number, limit):
    print(f"Multiplication Table for {number}")
    for i in range(1, limit + 1):
        result = number * i
        print(f"{number} x {i} = {result}")

# Example usage
number = 7  # Change this to any number you want the table for
limit = 10  # This is the limit to which you want the table
print_multiplication_table(number, limit)
