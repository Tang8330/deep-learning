"""Softmax."""

scores = [3.0, 1.0, 0.2]

import numpy as np

def softmax(x):
    """Compute softmax values for each sets of scores in x."""
    print "x", x
    denm = 0
    #sum = 0
    ret_list = []
    for num in x:
    	print "num", num
    	denm += np.exp(num)
    	print "denm", denm
    for num1 in x:
    	print np.exp(num1)/denm
    	ret_list.append(np.exp(num1)/denm)


    return np.array(ret_list)

    # ret = np.empty_like(x)
    # print "shape", x
    # for col in range(x.shape[1]):
    # 	denm = np.sum(np.exp(x[:, col]))
    # 	print ret[:, col]

    # print "hello", x

# print(softmax(scores))

# Plot softmax curves
import matplotlib.pyplot as plt
x = np.arange(-2.0, 6.0, 0.1)
scores = np.vstack([x, np.ones_like(x), 0.2 * np.ones_like(x)])

plt.plot(x, softmax(scores*10).T, linewidth=2)
plt.show()
