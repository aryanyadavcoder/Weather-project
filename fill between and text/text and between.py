import matplotlib.pyplot as plt

# range() का उपयोग
x = [i for i in range(1, 6)]
y = [10, 20, 15, 25, 30]

# Graph
plt.plot(x, y, marker="o", label="Data")

# plt.text() का उपयोग
for xi, yi in zip(x, y):
    plt.text(xi, yi, f"({xi},{yi})")

# plt.fill_between() का उपयोग
upper = [i + 5 for i in y]
lower = [i - 5 for i in y]

plt.fill_between(x, lower, upper, alpha=0.3, label="SD Range")

plt.title("All in One Example")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.grid(True)

plt.show()