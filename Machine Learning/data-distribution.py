import numpy
import matplotlib.pyplot as plt
print('data distribution')
x = numpy.random.uniform(0.0, 5.0, 250)
print(x)

print('Histogram')
x = numpy.random.uniform(0.0, 5.0, 250)
plt.hist(x, 5)
plt.show()

print('Big Data Distributions')
x = numpy.random.uniform(0.0, 5.0, 100000)

plt.hist(x, 100)
plt.show()