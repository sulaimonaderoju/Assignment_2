"""
Assignment 2
-------------------------------------

This program shows the following: import time and repeat the process 5 times,
the range function and a for loop, and assigning list of numbers to a variable
@Author: sulaimon
@Date: Jan 9 2024 
"""

import time

# Repeat the process five times
for _ in range(5):
    # Get the current time in minutes
    current_minute = time.localtime().tm_min

    # Check if the minute is odd or even
    if current_minute % 2 == 0:
        print(f"The current minute ({current_minute}) is even.")
    else:
        print(f"The current minute ({current_minute}) is odd.")

    # Wait for 60 seconds
#    time.sleep(60)
    
# The range function and a for loop
alphabet_string = 'abcdefghijklmnopqrstuvwxyz'

for letter in range(len(alphabet_string) - 1, 0, -2):
    print(alphabet_string[letter])

# Assigning list of numbers to a variable
import math

# Assign the list of numbers to a variable
numbers = [73.79693173, 41.76429734, 53.66368384, 24.60911367, 
           73.60414637, 62.26858213, 13.9670495, 70.97809816, 
           17.9978692, 56.10505197]

# Calculate the mean (average) of the numbers
mean = sum(numbers) / len(numbers)
print(mean)

# Calculate the squared differences from the mean
squared_diff = [(x - mean) ** 2 for x in numbers]
print(squared_diff)

# Calculate the population variance
population_variance = sum(squared_diff) / len(numbers)

# Calculate the population standard deviation using the math.sqrt() function
population_std_dev = math.sqrt(population_variance)

# Display the results
print("Population Variance:", population_variance)
print("Population Standard Deviation:", population_std_dev)