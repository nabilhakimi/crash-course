'''
#Plotting a Simple Line Graph
import matplotlib.pyplot as plt
plt.style.available

x_values = [1, 2, 3, 4, 5, 6, 7]
y_values = [1, 4, 9, 16, 25, 36, 49]

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, s=100)
#ax.plot(input_values, squares, linewidth=3)

# Set chart title and label axes.
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Set size of tick labels.
ax.tick_params(axis='both', labelsize=14)

plt.show()
'''
import matplotlib.pyplot as plt

x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

plt.style.use('seaborn-dark')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c='red', s=10)

# Set chart title and label axes.
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Set the range for each axis.
ax.axis([0, 1100, 0, 1100000])

plt.show()