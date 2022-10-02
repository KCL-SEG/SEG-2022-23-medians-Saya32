"""Median calculator."""
import statistics


while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
        
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break
print (statistics.median(numbers))