import matplotlib.pyplot as plt
import numpy as np
import math

# parsing the data
raw_data = []

filename = 'throw3'

def calc_resultant_force(row):
    return math.sqrt(row[1] ** 2 + row[2] ** 2 + row[3] ** 2)

with open('data/' + filename + '.txt', 'r') as raw_datafile:
    raw_datafile.readline()
    for line in raw_datafile:
        raw_data.append([int(x) for x in line.split()])

data = np.array(raw_data)

resultant_force_data = np.apply_along_axis(calc_resultant_force, 1, data)

plt.figure(figsize=(20, 10))

plt.subplot(2, 1, 1)
plt.title("raw accelerometer data in 3 axes")

plt.plot(data[:, 0], data[:, 1], label='acc in x')
plt.plot(data[:, 0], data[:, 2], label='acc in y')
plt.plot(data[:, 0], data[:, 3], label='acc in z')

plt.legend(loc=2)

plt.ylabel('acceleration/ mg')
plt.xlabel('time/ ms')

plt.subplot(2, 1, 2)
plt.title("resultant force")

plt.plot(data[:, 0], resultant_force_data, label='acc in x')

plt.legend(loc=2)

plt.ylabel('acceleration/ mg')
plt.xlabel('time/ ms')

plt.savefig('plots/plot_' + filename + '.png')
plt.show()
