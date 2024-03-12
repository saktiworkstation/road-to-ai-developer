print('\n- Histogram')
import sys
import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
import numpy as np

x = np.random.normal(170, 10, 250)

plt.hist(x)
plt.show()
plt.savefig(sys.stdout.buffer)
sys.stdout.flush()