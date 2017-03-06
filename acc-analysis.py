import matplotlib.pyplot as plt
import numpy as np

# parsing the data
raw_data = []

filename = 'throw3'


with open('data/'+filename+'.txt', 'r') as raw_datafile:
    raw_datafile.readline()
    for line in raw_datafile:
        raw_data.append([int(x) for x in line.split()])

data = np.array(raw_data)

plt.plot()

plt.subplot(2,1,1)
plt.title("unadjusted values")

plt.plot(data[:,0],data[:,1], label='acc in x')
plt.plot(data[:,0],data[:,2], label='acc in y')
plt.plot(data[:,0],data[:,3], label='acc in z')

plt.legend(loc=1)

plt.ylabel('acceleration/ mg')
plt.xlabel('time/ ms')

data[:,1]-=data[0,1]
data[:,2]-=data[0,2]
data[:,3]-=data[0,3]

plt.subplot(2,1,2)
plt.title("change in acceleration")

plt.plot(data[:,0],data[:,1], label='acceleration in x')
plt.plot(data[:,0],data[:,2], label='acceleration in y')
plt.plot(data[:,0],data[:,3], label='acceleration in z')

plt.savefig('plots/plot_'+filename+'.png')
plt.show()
