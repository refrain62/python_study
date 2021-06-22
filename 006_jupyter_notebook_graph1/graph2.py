%matplotlib inline

import numpy as np
import matplotlib.pyplot as plt

x = np.random.uniform( 0, 1, 100000 )
plt.hist( x, bins=100 )
plt.show()
