import sys
import math

def load_data(filepath:str, column:int)->tuple[list, int]:
    #Opens the file, loops through each line and splits by tabs, handles IndexError/ValueError, returns tuple containing list of float values and total number of rows 
    numbers = []
    total_count = 0

    try: 
        with open(filepath, 'r') as infile: 
            line_num = 0
            for line in infile: 
                line_num += 1
                total_count += 1
                line = line.strip()
                if not line: 
                    total_count -= 1    #not counting empty lines in row count
                    continue
                parts = line.split("\t")
                #IndexError 
                try: 
                    val_str = parts[column]
                except IndexError: 
                    print(f"Exiting: There is no valid 'list index' in column {column} in line {line_num} in file: {filepath}")
                    sys.exit(1)
                #Converting to float and ValueError 
                try: 
                    val_float = float(val_str)
                    if not math.isnan(val_float): 
                        numbers.append(val_float)
                except ValueError: 
                    continue
    except FileNotFoundError: 
        print(f"Error: The file {filepath} was not found")
        sys.exit(1)
    return numbers, total_count
                

def calculate_average(numbers:list)->float:
    #Calculates average of the list of numbers 
    if not numbers: 
        return 0.0
    return sum(numbers) / len(numbers)

def get_max_and_min(numbers:list)->tuple[float, float]:
    #Returns tuple with max and min values in the list
    if not numbers: 
        return 0.0, 0.0
    return max(numbers), min(numbers)

def calculate_variance(numbers:list)->float:
    #Calculates the sample variance of the numbers in the list
    n = len(numbers)
    if n <= 1: 
        return 0.0
    avg = calculate_average(numbers)
    return sum((x - avg) ** 2 for x in numbers) / (n - 1)

def calculate_std_dev(numbers:list)->float:
    #Calculates standard deviation of the numbers in the list 
    variance = calculate_variance(numbers)
    return math.sqrt(variance)

def calculate_median(number:list)->float:
    #Calculates median of the numbers in the list 
    if not number: 
        return 0.0
    sorted_numbers = sorted(number)
    n = len(sorted_numbers)
    mid = n // 2
    if n % 2 == 0: 
        return (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2
    else: 
        return sorted_numbers[mid]


#MAIN---------------------------------------------------------------------------------------------------


