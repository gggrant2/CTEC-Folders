#Genesis Grant
#CTEC450 


def find_min_max(numbers):
    """Find and return the minimum and maximum values from a list of numbers."""
    if not numbers:
        return None, None
    min_val = max_val = numbers[0]
    for num in numbers[1:]:
        if num < min_val:
            min_val = num
        if num > max_val:
            max_val = num
    return min_val, max_val

def main():
    # Input file name (you can change this as needed)
    input_file = "input.txt"
    
    try:
        # Read numbers from the input file
        with open(input_file, 'r') as file:
            numbers = [float(line.strip()) for line in file.readlines()[:5]]
        
        if len(numbers) < 5:
            print("Error: The input file must contain at least 5 numbers.")
            return
        
        # Find min and max
        min_val, max_val = find_min_max(numbers)
        
        # Print the results
        print(f"The numbers are: {numbers}")
        print(f"Minimum value: {min_val}")
        print(f"Maximum value: {max_val}")
        
    except FileNotFoundError:
        print(f"Error: The file '{input_file}' was not found.")
    except ValueError:
        print("Error: The file contains non-numeric data.")

if __name__ == "__main__":
    main()