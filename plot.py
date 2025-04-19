import matplotlib.pyplot as plt
x = [2,3]
y = [6,7]
z = [4,5]
t = [0,1]

plt.plot([x[0],x[1]],[y[0],y[1]],label="Recta")
plt.plot([z[0],z[1]],[t[0],t[1]])
plt.legend(loc="best")
plt.show()