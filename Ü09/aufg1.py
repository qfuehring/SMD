import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize
from scipy.misc import factorial


def poisson(k, l):#k is poisson order, l is fittingparameter
    return (l**k/factorial(k)) * np.exp(-l)

def negLogLikelihood(params, data):
    l= - np.sum(np.log(poisson(data, params[0])))
    return l

data = [8,9,13]

# minimize the negative log-Likelihood

result = minimize(negLogLikelihood,  # function to minimize
                  x0=[1],     # start value
                  args=(data,),      # additional arguments for function
                  method='Powell',   # minimization method, see docs
                  )
# result is a scipy optimize result object, the fit parameters
# are stored in result.x

print("Der Fitparameter für die Poissonverteilung:  ",result.x)

# plot the fitted Poisson
x = np.linspace(0, 20, 1000)

plt.hist(data, bins=np.arange(15) - 0.5, normed=True)
plt.plot(x, poisson(x, result.x), 'r-', lw=2)
plt.show()
