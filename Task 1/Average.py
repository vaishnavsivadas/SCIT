import numpy as np
import matplotlib.pyplot as plt
for i in range(100):
    p=np.random.poisson(4,1000)
    b=np.random.normal(0,0.1,1000)
    arr=[]
    for i in range(100):
        a=np.random.randint(0,1000)
        avg=(p[a]+b[a])/2
        arr.append(avg)
    plt.hist(arr,density=True)
plt.savefig("Graphs/Average/Average.png")        
plt.show()