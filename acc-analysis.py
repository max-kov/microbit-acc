import matplotlib.pyplot as plt

# parsing the data
raw_data = []

filename = 'throw1.txt'

timestamps = []
accx = []
accy = []
accz = []

with open('data/'+filename, 'r') as raw_datafile:
    raw_datafile.readline()
    for line in raw_datafile:
        raw_data.append([int(x) for x in line.split()])

for point in raw_data:
    timestamps.append(point[0])
    accx.append(point[1])
    accy.append(point[2])
    accz.append(point[3])

# plot

plt.plot(timestamps,accx,timestamps,accy,timestamps,accz)
plt.show()