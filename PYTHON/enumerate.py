fruits = ['apple', 'banana', 'cherry']

for index, fruit in enumerate(fruits):
    print(index, fruit)

print('\n')

for index, fruit in enumerate(fruits, start=1):
    print(index, fruit)
