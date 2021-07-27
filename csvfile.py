import csv

filename = 'uk-500.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

#Printing the Headers and Their Positions
    for index, column_header in enumerate(header_row):
        print(index, column_header)

# Get high temperatures from this file.
    cities = []
    for row in reader:
        city = str(row[4])
        cities.append(city)

print(cities)