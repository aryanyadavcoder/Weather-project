import time
import matplotlib.pyplot as plt

# 1. Turn on interactive mode
plt.ion()

x = [1, 2, 3, 4]
y1 = [1, 4, 9, 16]

# 2. Draw the first plot
plt.plot(x, y1, label="Initial Plot", color="blue")
plt.legend()
plt.show()  # In interactive mode, this does NOT block execution

# Simulate a delay (e.g., waiting for new data calculation)
print("Waiting 2 seconds before adding the next plot...")
time.sleep(5)

# 3. Add the second plot to the existing open window
y2 = [2, 4, 6, 8]
plt.plot(x, y2, label="Added Later", color="red", linestyle="--")
plt.legend()

# 4. Force matplotlib to redraw the figure with the new data
plt.draw()

# Keep the window open at the end of the script
plt.ioff()
plt.show()
