import matplotlib.pyplot as plt

x = [1, 2, 3]
y = [10, 20, 15]

plt.plot(x, y, marker="o")

plt.text(2, 20, "Highest")

plt.show()

 # 2
 
 
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 25, 30]

plt.plot(x, y)

plt.fill_between(x, y, alpha=0.3)

plt.show()