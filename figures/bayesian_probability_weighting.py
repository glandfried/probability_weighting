import numpy as np
import scipy.stats as s
import matplotlib.pyplot as plt

a=100;b=100
grilla = np.linspace(0, 1,10001)
y = s.beta.pdf(grilla, a, b)
plt.plot(grilla, y, 'r-', lw=5, alpha=0.6, label='beta pdf')
grilla[np.argmax(y)]

s.beta.stats(a, b)

total = 100
maximum_a_posteriori = []
x = np.linspace(0, 1,total + 1)
mean = []
for i in x:#i=0.05
    a = 0.00001; b = 0.00001
    caras = int(total*i)
    a += caras; b += total-caras
    #mean.append(float(s.beta.stats(a, b)[0]) )
    y = s.beta.pdf(grilla, a, b)
    maximum_a_posteriori.append(grilla[np.argmax(y)])

#plt.plot(x,mean)
plt.plot(x,maximum_a_posteriori)
plt.plot(x,x)
