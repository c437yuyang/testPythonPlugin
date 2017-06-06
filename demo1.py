import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0, 2 * np.pi, num=1000)
plt.plot(x, np.sin(x),'r2')
plt.show()