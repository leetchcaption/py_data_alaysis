
import numpy as np
import matplotlib.pyplot as plt

import wordcloud
x = np.linspace(0, 1)
y = np.sin(4 * np.pi * x) * np.exp(-5 * x)
plt.plot(x, y,'o')
plt.show()