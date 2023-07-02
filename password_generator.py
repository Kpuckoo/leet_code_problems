import random
import string

total = string.ascii_letters + string.digits + string.punctuation
length = 16
password = "".join(random.sample(total, length))

print(password)

with open('passwords.txt', 'a') as f:
    f.write(password + '\n')
