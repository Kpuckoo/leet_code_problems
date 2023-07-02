import random
import string
import os

total = string.ascii_letters + string.digits + string.punctuation
length = 16

# The number of passwords to generate
num_passwords = 1

# File to store passwords
file_name = 'passwords.txt'

# Check if the file exists
if os.path.exists(file_name):
    # If the file exists, read the last line and get the number
    with open(file_name, 'r') as f:
        lines = f.readlines()
        last_num = int(lines[-1].split('.')[0]) if lines else 0
else:
    # If the file doesn't exist, start from 0
    last_num = 0

with open(file_name, 'a') as f:
    for i in range(last_num + 1, last_num + num_passwords + 1):
        password = "".join(random.sample(total, length))
        print(password)

        # Append the password to the text file
        f.write(str(i) + '. ' + password + '\n')
