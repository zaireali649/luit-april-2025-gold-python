# Import standard libraries for random number generation, date/time, OS operations, and math functions
import random
import datetime
import os
import math

# import a local library
import hello_world

# import an external library
# if ModuleNotFoundError, use pip to install
import matplotlib.pyplot as plt
import emoji  # Library for working with emojis

# Generate a random integer between 0 and 10 (inclusive)
random_number = random.randint(0, 10)
print(f"Random number (0-10): {random_number}")

# Get the current date and time
now = datetime.datetime.now()
# Format the date/time as a string like '2025-04-24 19:45:00'
formatted_time = now.strftime("%Y-%m-%d %H:%M:%S")
print(f"Current time: {formatted_time}")

# Get the current working directory (the folder where this script is running)
cwd = os.getcwd()
print(f"Current working directory: {cwd}")

# Print the mathematical constant pi
print(f"Value of pi: {math.pi}")
# Print the square root of 16
print(f"Square root of 16: {math.sqrt(16)}")

# Sample data: x values from 1 to 5, y values are squares of x
x = [1, 2, 3, 4, 5]
y = [i**2 for i in x]

# Create the plot
plt.plot(x, y, marker='o')  # 'o' adds circle markers at data points

# Add titles and labels
plt.title("Square Numbers")
plt.xlabel("X Values")
plt.ylabel("Y = X Squared")

# Display the plot
plt.grid(True)
plt.show()

# Convert text aliases to emoji characters
message = emoji.emojize("Python is :fire: and :snake:!", language='alias')
print(message)

# Convert emoji characters back to aliases
back_to_text = emoji.demojize(message)
print(back_to_text)
