import numpy as np
import scipy
import matplotlib.pyplot as plt

a=2;b=3
x = np.linspace(0, 1,101)
y = scipy.stats.beta.pdf(x, a, b)
plt.plot(x, y, 'r-', lw=5, alpha=0.6, label='beta pdf')

MAP = x[np.argmax(y)]
