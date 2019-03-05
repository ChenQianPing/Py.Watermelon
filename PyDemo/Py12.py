import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10,10,1000)
y = x ** 2 - 2 * x+ 1
plt.plot(x, y)
plt.title("matplotlib")
plt.xlabel("height")
plt.ylabel("width")
# 设置图例
plt.legend(["X","Y"], loc="upper right")
plt.grid(True)
plt.show()
