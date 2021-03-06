import numpy as np
import matplotlib.pyplot as plt

def f1(t):
    return np.exp(-t)*np.cos(2*np.pi*t)

def f2(t):
    return np.sin(2*np.pi*t)*np.cos(3*np.pi*t)

t = np.arange(0.0,5.0,0.02)


plt.figure()
plt.plot(t,f1(t),"g-",label="$f(t)=e^{-t} \cdot \cos (2 \pi t)$")
plt.plot(t,f2(t),"r-.",label="$g(t)=\sin (2 \pi t) \cos (3 \pi t)$",linewidth=2)

plt.axis([0.0,5.01,-1.0,1.5])
plt.xlabel("t")
plt.ylabel("v")
plt.title("a simple example")

plt.grid(True)
plt.legend()
plt.show()