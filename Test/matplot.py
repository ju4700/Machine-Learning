import matplotlib.pyplot as plt

input = [1, 2, 3, 4, 5] #X
sq = [1, 4, 9, 16, 25] #Y

fig, ax = plt.subplots()
ax.scatter(input, sq, s=100, color='red') #s is size of the dot
ax.plot(input, sq, linewidth=3)

ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)
ax.ticklabel_format(style='plain') #Remove scientific notation

plt.show()
plt.savefig('squares_plot.png', bbox_inches='tight') #Save the plot as a png file
