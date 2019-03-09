import numpy as np
import matplotlib.pyplot as plt
import scipy.interpolate

ultrasound_data = np.genfromtxt('./ultrasonidos.csv',delimiter=';',usecols=np.arange(0,11),skip_header=1)
ultrasound_data = np.transpose(ultrasound_data)
ultrasound_data = ultrasound_data[1::]
theoric_data = [20,40,60,80,100,120,150,180,210,240]
plt.figure(1)
for i,arr in enumerate(ultrasound_data):
    print(np.mean(arr),np.std(arr))
    plt.plot(arr)
    #plt.errorbar(arr)
    plt.plot([theoric_data[i]]*len(arr),"r--")

x_pos2 = np.arange(0,len(ultrasound_data),1)
x_pos = np.arange(0,len(ultrasound_data))
means = [np.mean(i) for i in ultrasound_data]
stds = [np.std(i) for i in ultrasound_data]


p = np.polyfit(theoric_data,means,1)
f = np.poly1d(p)

fig,ax = plt.subplots()

ax.set_xlabel("Distancia teórica (cm)")
ax.set_ylabel("Distancia real (cm)")
ax.plot(theoric_data,means,"b.")
new_x = np.linspace(0,250,250)
new_y = f(new_x)
print(p)
ax.plot(new_x,new_y,"r--")
ax.grid()


fig,ax = plt.subplots()


ax.bar(x_pos2,means,yerr=stds,align='center',alpha=1,ecolor='black',color="lightblue",capsize=10)
ax.set_ylabel("Media distancia real (cm)")
ax.set_xticks(x_pos)
ax.set_xticklabels([str(x) for x in theoric_data])
ax.set_xlabel("Distancia teórica")

ax.bar(x_pos2,theoric_data,alpha=1,color='red',width=0.2)


plt.show()