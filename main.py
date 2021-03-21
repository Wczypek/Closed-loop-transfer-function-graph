import matplotlib.pyplot as plt
import numpy as np

t1 = 50
l=2.5
h=0.001
kroki=int(t1/h)

amp = 1
a = 0.5
b = 0.5
k = 0.5
m = 0.5

t = np.zeros(kroki)
for x in range(kroki):
    t[x] = x*h

u = amp * np.sign(np.sin(2*np.pi*t/(t1/l)))

Y2p =  np.zeros(kroki)
Y1p =  np.zeros(kroki)
Y =  np.zeros(kroki)
#warunki poczatkowe

Y2p[0] = 0
Y1p[0] = 0
Y[0] = 0


for i in range(kroki-1):
    Y2p[i] = -Y1p[i] * a - Y[i] * k * b * m + u[i] * k * b
    Y1p[i+1] = Y1p[i] + h/1 *Y2p[i]
    Y[i+1] = Y[i] + h/1 * Y1p[i] + h*h/2 * Y2p[i]


plt.plot(t, Y)
plt.plot(t, u)
plt.show()
