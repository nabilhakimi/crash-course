'''
alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'fast'}
print(f"Original position: {alien_0['x_position']}")
# Move the alien to the right.
# Determine how far to move the alien based on its current speed.
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
# This must be a fast alien.
    x_increment = 3
# The new position is the old position plus the increment.
alien_0['x_position'] = alien_0['x_position'] + x_increment
print(f"New position: {alien_0['x_position']}")

favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}
person = input('Name: ')
language = favorite_languages.get('[person].title()', 'No point value assigned.')
print(f"{person.title()}'s favorite language is {language}.")

alien_0 = {'color': 'green', 'speed': 'slow'}
point_value = alien_0.get('points', 'No point value assigned.')
print(point_value)

user_0 = {
'username': 'efermi',
'first': 'enrico',
'last': 'fermi',
}
for key, value in user_0.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")

favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}
for name, language in favorite_languages.items():
    print(f"\n{name.title()}'s favorite language is {language.title()}.")
'''
favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}
'''
friends = ['phil', 'edward']
for name in favorite_languages.keys():
    print(name.title())

if name in friends:
    language = favorite_languages[name].title()
    print(f"\t{name.title()}, I see you love {language}!")

for name in sorted(favorite_languages.keys()):
    print(f"\n{name.title()}, thank you for taking the poll.")

print("\nThe following languages have been mentioned:")
for language in sorted(set(favorite_languages.values())):
    print(language.title())

aliens = []

for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[0:7]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien in aliens[0:3]:
        alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15
for alien in aliens[:10]:
    print(alien)
print('...')
# Show how many aliens have been created.
print(f"Total number of aliens: {len(aliens)}")

# Store information about a pizza being ordered.
pizza = {
'crust': 'thick',
'toppings': ['mushrooms', 'extra cheese'],
}
# Summarize the order.
print(f"You ordered a {pizza['crust']}-crust pizza "
"with the following toppings:")
for topping in pizza['toppings']:
    print("\t" + topping)

#list with two values
favorite_languages = {
'jen': ['python', 'ruby'],
'sarah': ['c'],
'edward': ['ruby', 'go'],
'phil': ['python', 'haskell'],
}
for name, languages in favorite_languages.items():
    print(f"\n{name.title()}'s favorite languages are:")
    for language in languages:
        print(f"\t{language.title()}")

#a dictionary in a dictionary
users = {
'aeinstein': {
'first': 'albert',
'last': 'einstein',
'location': 'princeton',
},
'mcurie': {
'first': 'marie',
'last': 'curie',
'location': 'paris',
},
}
for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']

    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")
'''