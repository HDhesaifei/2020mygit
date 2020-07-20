import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

x = np.arange(0,1,0.05)
print(x)
y = np.sin(2*np.pi*x)
print(y)

plt.plot(x,y,'b--*',label='sin')
plt.title("My First Plot")
plt.xlabel("x label")
plt.ylabel("y label")
plt.legend(loc='best')
plt.show()

fig,ax=plt.subplots(2,2)
ax[0,1].plot(x,y)
plt.show()

y2 = np.cos(2*np.pi*x)
print(y2)

fig,ax=plt.subplots()
ax.plot(x,y,'g--*',label='sin')
ax.plot(x,y2,'r--o',label='cos')
ax.set(title="My First Plot")
legend = ax.legend(loc='best')
plt.show()

fig.savefig('myfig.png')
