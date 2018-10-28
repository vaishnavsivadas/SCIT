import numpy as np
import matplotlib.pyplot as plt 
for i in range(3):
    b= np.random.normal(1,0.1,1000)
    np.savetxt("Data Sets/Normal "+str(i),b,delimiter=",")
    plt.xlabel("x")
    plt.ylabel("P(X)=x")
    plt.hist(b,density=True)
    plt.savefig("Graphs/Normal/Normal "+str(i)+".png")
    plt.show()