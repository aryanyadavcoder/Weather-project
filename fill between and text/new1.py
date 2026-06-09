import matplotlib.pyplot as plt

x = [i for i in range(1, 6)]
y = [10, 20, 15, 25, 30]

# Line graph
plt.plot(x, y, marker="o")

for xi, yi in zip(x, y):
    plt.text(xi, yi, str(yi))

plt.fill_between(x, y, alpha=0.3)

plt.title("Combined Example")
plt.xlabel("X")
plt.ylabel("Y")

plt.show()