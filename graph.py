import matplotlib.pyplot as plt

x = [x for x in range(-11,10)]
y = [x**3 for x in range(-11,10)]

plt.plot(x,y)
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("Plot for y = x^3")
plt.grid()
plt.show()
