import numpy as np
import matplotlib.pyplot as plt
import scipy.interpolate

light_data = np.genfromtxt('./luz.csv',delimiter=';',usecols=np.arange(0,11),skip_header=1)
light_data = np.transpose(light_data)
light_data = light_data[1::]
theoric_data = [20,40,60,80,100,120,150,180,210,240]

#plt.figure(1)
for i,arr in enumerate(light_data):
    print(np.mean(arr),np.std(arr))
    #plt.plot(arr)
    #plt.errorbar(arr)
    #plt.plot([theoric_data[i]]*len(arr),"r--")

x_pos2 = np.arange(0,len(light_data),1)
x_pos = np.arange(0,len(light_data))
means = [np.mean(i) for i in light_data]
stds = [np.std(i) for i in light_data]

#plt.figure(2)
#plt.plot(theoric_data)

fig,ax = plt.subplots()

ax.bar(x_pos2,means,yerr=stds,align='center',alpha=1,ecolor='black',color="lightblue",capsize=10)
ax.set_ylabel("Intensidad sensor luz")
ax.set_xticks(x_pos)
ax.set_xticklabels([str(x) for x in theoric_data])
ax.set_xlabel("Distancia(cm)")

#+ax.bar(x_pos2,theoric_data,alpha=1,color='red',width=0.2)

fig2,ax2 = plt.subplots()
ax2.plot(means,theoric_data)
ax2.set_ylabel("Distancia(cm)")
ax2.set_xlabel("Intensidad de la luz en el sensor")
ax2.grid()


p = np.polyfit(theoric_data,means,3)
f = np.poly1d(p)
print(p)
new_y = np.linspace(0,250,250)
new_x = f(new_y)
fig3,ax3 = plt.subplots()
ax3.plot(means,theoric_data)
ax3.plot(new_x,new_y,"r--")
ax3.set_ylabel("Distancia(cm)")
ax3.set_xlabel("Intensidad de la luz en el sensor")
ax3.grid()
plt.show()