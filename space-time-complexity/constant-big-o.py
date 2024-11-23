
def main():
    """Main function to handle user input and output."""
    # Define an array with some numbers
    numbers = [2, 4, 6, 8, 10]

    # Print the array for user reference
    print("Array:", numbers)

    # Get input from the user for the index
    try:
        index = int(input(f"Enter the index of the number you want to square(0-{len(numbers)}): "))

        # Check if the index is valid
        if 0 <= index < len(numbers):
            result = square(numbers[index])
            print(f"The square of the number at index {index} ({numbers[index]}) is: {result}")
        else:
            print("Error: Index out of range. Please enter a valid index.")
    except ValueError:
        print("Error: Please enter a valid integer.")

def square(number):
    """Returns the square of the given number."""
    return number ** 2

# Run the main function
if __name__ == "__main__":
    main()