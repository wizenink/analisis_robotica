import numpy as np
import matplotlib.pyplot as plt
import scipy.interpolate
import os

num_samples = 5

pot_data = np.genfromtxt('./motores/potencia.csv',delimiter=';',usecols=np.arange(0,4),skip_header=1)

pot = np.array([10,50,100])

data1 = np.transpose(pot_data[:num_samples])
data2 = np.transpose(pot_data[num_samples:num_samples*2])
data3 = np.transpose(pot_data[num_samples*2:])

cm1 = np.mean(data1[3])
cm2 = np.mean(data2[3])
cm3 = np.mean(data3[3])

t1 = np.mean(data1[2])
t2 = np.mean(data2[2])
t3 = np.mean(data3[2])

s1 = cm1/t1
s2 = cm2/t2
s3 = cm3/t3

print(s1)
print(s2)
print(s3)

fig,ax = plt.subplots()
ax.plot(pot,[s1,s2,s3])
ax.set_xlabel("Potencia del motor")
ax.set_ylabel("Velocidad real(cm/s)")
ax.grid()
plt.show()

