import numpy as np
import matplotlib as plt
for i in range(3):
    p= np.random.poisson(lam=6,size=1000)
    np.savetxt("Data Sets/Poisson data set "+str(i),p,delimiter=",")
    plt.xlabel("x")
    plt.ylabel("P(X)=x")
    plt.hist(p,density=True)
    plt.savefig("Graphs/Poisson/Poisson "+str(i)+".png")
    plt.show()