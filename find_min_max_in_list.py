lst = []
num = int(input('How many numbers: '))

for n in range(num):
    numbers = int(input('Enter number '))
    lst.append(numbers)

print("Maximum number in the list is :", max(lst), "\nMinimum number in the list is :", min(lst))
