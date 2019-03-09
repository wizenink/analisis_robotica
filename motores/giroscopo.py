import numpy as np
import matplotlib.pyplot as plt
import scipy.interpolate
import os

num_samples = 5

gir_data = np.genfromtxt('./motores/giroscopo.csv',delimiter=';',usecols=np.arange(0,3),skip_header=0)

pot = np.array([90,180,270])

data1 = np.transpose(gir_data[:num_samples])
data2 = np.transpose(gir_data[num_samples:num_samples*2])
data3 = np.transpose(gir_data[num_samples*2:])

gir1 = np.mean(data1[1])
gir2 = np.mean(data2[1])
gir3 = np.mean(data3[1])

t1 = np.mean(data1[2])
t2 = np.mean(data2[2])
t3 = np.mean(data3[2])


dgir1 = np.std(data1[1])
dgir2 = np.std(data2[1])
dgir3 = np.std(data3[1])

dt1 = np.std(data1[2])
dt2 = np.std(data2[2])
dt3 = np.std(data3[2])

print([gir1,gir2,gir3])
print([t1,t2,t3])
print("STD:")

print([dgir1,dgir2,dgir3])
print([dt1,dt2,dt3])
fig,ax = plt.subplots()
ax.plot([gir1,gir2,gir3],[t1,t2,t3])
ax.set_xlabel("Ángulo medido por el giróscopo (º)")
ax.set_ylabel("Ángulo medido por el transportador (º)")
ax.grid()
plt.show()

