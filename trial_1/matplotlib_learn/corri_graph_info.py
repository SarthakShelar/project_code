import matplotlib.pyplot as plt
import tkinter as tk


fig, ax1 = plt.subplots()
ys = [35, 42, 39, 45, 36, 49, 45]

xs = [1, 2, 3, 4, 5, 6, 7]
ax1.plot(xs, ys)
ax1.set_title("Humidity")
ax1.set_xlabel("Humidity(in percetange)")
ax1.set_ylabel("Time(in Second)")
#plt.show()




fig1, ax1 = plt.subplots()
ys = [20, 42, 39, 45, 36, 49, 45]

xs = [1, 2, 3, 4, 5, 6, 7]
ax1.plot(xs, ys)
ax1.set_title("Temperature")
ax1.set_ylabel("Temerature(in celcius)")
ax1.set_xlabel("Time(in Second)")
#plt.show()



