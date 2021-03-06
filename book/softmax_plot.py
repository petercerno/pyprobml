
# Plot the softmax function.


import numpy as np
import matplotlib.pyplot as plt
import os
figdir = os.path.join(os.environ["PYPROBML"], "figures")
def save_fig(fname): plt.savefig(os.path.join(figdir, fname))


from scipy.misc import logsumexp
 
def softmax(a):
  e = np.exp((1.0 * np.array(a)))
  return e / np.sum(e)
  

T = [100, 2, 1]
a = np.array([3, 0, 1]);
ind = [1, 2, 3]

plt.figure(figsize=(12,4))
for i in range(len(T)):
    plt.subplot(1,3,i+1)
    plt.bar(ind, softmax(a / T[i]))
    plt.title('T = %d' % T[i])
    plt.ylim(0, 1)
    ax = plt.gca()
    ax.set_xticklabels([])
    

fname = 'softmax_temp.pdf'
print(fname)
save_fig(fname)
plt.show()




