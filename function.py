'''
def greet_user():
    """Display a simple greeting."""
    print("Hello!")
greet_user()

#function with information
username = input("Please enter your name: ")
def greet_user(username):
    """Display a simple greeting."""
    print(f"Hello, {username.title()}!")
greet_user(username)

#Positional Arguments
animal_type = input("Type of animal: ")
pet_name = input("Name: ")
def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
describe_pet(animal_type, pet_name)

def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
describe_pet(animal_type='hamster', pet_name='harry')

#return values
first_name = input("First name: ")
last_name = input("Last name: ")
def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()
student = get_formatted_name(first_name, last_name)
print(student)

#return values (optional middle name)
first_name = input("First name: ")
last_name = input("Last name: ")
middle_name = input("Middle name: ")
def get_formatted_name(first_name, last_name, middle_name=''):
    """Return a full name, neatly formatted."""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()
student1 = get_formatted_name(first_name, last_name)
print(student1)
student2 = get_formatted_name(first_name, last_name, middle_name)
print(student2)

#Returning a Dictionary
first_name = input("First name: ")
last_name = input("Last name: ")
age = int(input("Age: "))
def build_person(first_name, last_name, age):
    """Return a dictionary of information about a person."""
    person = {'first name': first_name.title(), 'last name': last_name.title(), 'age': age}
    return person
student = build_person(first_name, last_name, age)
print(student)

#Using a Function with a while Loop
def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()
while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")
    f_name = input("First name: ")
    if f_name == 'q':
        break
    l_name = input("Last name: ")
    if l_name == 'q':
        break
    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}!")

#Passing a List
def greet_users(names):
    """Print a simple greeting to each user in the list."""
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)
usernames = ['muhamad', 'nabil', 'hakimi']
greet_users(usernames)

#Modifying a List in a Function
# Start with some designs that need to be printed.
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []
# Simulate printing each design, until none are left.
# Move each design to completed_models after printing.
while unprinted_designs:
    current_design = unprinted_designs.pop()
    print(f"Printing model: {current_design}")
    completed_models.append(current_design)
# Display all completed models.
print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model)

# Start with some designs that need to be printed.
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []
def print_models(unprinted_designs, completed_models):
    """
    Simulate printing each design, until none are left.
    Move each design to completed_models after printing.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """Show all the models that were printed."""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

#Preventing a Function from Modifying a List
print_models(unprinted_designs[:], completed_models)
show_completed_models(completed_models)

#Passing an Arbitrary Number of Arguments
def make_pizza(*toppings):
    """Summarize the pizza we are about to make."""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

#Mixing Positional and Arbitrary Arguments
def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
'''
#Using Arbitrary Keyword Arguments(**kwargs)
def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first.title()
    user_info['last_name'] = last.title()
    return user_info

user_profile = build_profile('albert', 'einstein',
location='Princeton',
field='Physics')

print(user_profile)