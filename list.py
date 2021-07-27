'''
name = ['Nabil', 'Hakimi']
print(name)
popped_name = name.pop()
print(name)
print(popped_name)

a = int(input('Enter first number: '))
b = int(input('Enter second number: '))
print(a + b)

motorcycles = ['honda', 'yamaha', 'suzuki']
del motorcycles[2]
print(motorcycles)

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.insert(2, 'ford')
print(cars[-1])

friends = ['alice', 'david', 'carolina']
for friend in friends:
    print(f"{friend.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {friend.title()}.\n")

print("Thank you, everyone. That was a great magic show!")

for value in range(1, 50, 5):
    print(value)

numbers = list(range(1, 6))
print(numbers)

squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)
print(squares)

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum(digits))

squares = [value**2 for value in range(1, 11)]
print(squares)

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[1:-1])

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)

print("\n My friend's favorite foods are:")
print(friend_foods)

#Tuple
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])
'''
dimensions = (200, 50)
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print("\n Modified dimensions:")
for dimension in dimensions:
    print(dimension)
