import matplotlib.pyplot as plt
import numpy as np
import math

print("Hello World")

#グラフ横軸
x = range(1,1000)
#Generate sin wave
y = np.array([math.sin(math.radians(ms)) for ms in x])


#Graph
plt.plot(x,y,label='sin', color='blue')
plt.show();

