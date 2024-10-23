import numpy
import matplotlib.pyplot as plt
font = {"fontname": "DM Sans"}
data = numpy.random.randint(10,50, 10)
print (data)
x = numpy.linspace(1,10,10)
print (x)
plt.bar(x,data, color = "#C0E0B2")
plt.plot(x,data,".", color = "#71995F", markersize = 15)

p = numpy.polyfit(x,data,9)
p2 = numpy.poly1d(p)
print (p2)
x1 = numpy.linspace(1,10,200)
plt.plot(x1,p2(x1), "--", color = "#5F8368")
plt.ylim(0,max(data)+5)
plt.title("Water Usage Graph",**font)
plt.xlabel("Date",**font)
plt.ylabel("Carbon Produced (metric tons)")
plt.legend(["current week", "previous week"])
plt.show()