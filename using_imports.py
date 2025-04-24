import random
import datetime
import os
import math

random_number = random.randint(0, 10)
print(f"Random number (0-10): {random_number}")

now = datetime.datetime.now()
formatted_time = now.strftime("%Y-%m-%d %H:%M:%S")
print(f"Current time: {formatted_time}")

cwd = os.getcwd()
print(f"Current working directory: {cwd}")

print(f"Value of pi: {math.pi}")
print(f"Square root of 16: {math.sqrt(16)}")
