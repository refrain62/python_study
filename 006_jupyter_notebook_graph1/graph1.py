%matplotlib inline

import numpy as np
import matplotlib.pyplot as plt

y = np.random.normal( 0, 0.333, 100000 )
plt.hist( y, bins=100 )
plt.show()

