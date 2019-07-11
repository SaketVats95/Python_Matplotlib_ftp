l=[i for i in range(1,20) if i%2==0]
k=[i for i in range(10)]

import matplotlib.pyplot as plt

'''
plt.plot([5,6,10,13],label='L1')
plt.plot([1,2,3,4],label='L2')'''
plt.xlabel('x')
plt.ylabel('y')
plt.title('Graph\nRepesent X_Y Axis')
plt.legend()
plt.show()
