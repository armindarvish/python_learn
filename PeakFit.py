import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


def linear(x, m, b):
    return m * x + b


def exponential(x, a, b, c):
    return a * (b ** x) + c


def natural_exp(x, a, b, c):
    return a * np.exp(b * x) + c


x_linear = np.linspace(1, 10, 10)
y_linear = np.linspace(5, 200, 10)
y_linear_noise = 0.1*(np.random.normal(len(x_linear)))
y_linear += y_linear_noise

popt, pcov = curve_fit(linear, x_linear, y_linear)

fig1 = plt.figure()
ax = fig1.add_subplot()
ax.plot(x_linear, y_linear, 'ro')
ax.set_xlabel("x", fontsize=14)
ax.set_ylabel("y", fontsize=14)
ax.plot(x_linear, linear(x_linear, *popt), 'k',
        label="y= %0.2fx + (%0.2f)" % (popt[0], popt[1]))
ax.legend(loc='best')
fig1.show()

x_exp = np.linspace(1, 20, 50)
y_exp = 2*(np.exp(x_exp))+10
y_exp_noise = 0.1*(np.random.normal(len(x_exp)))
y_exp += y_exp_noise

popt, pcov = curve_fit(exponential, x_exp, y_exp)

fig2 = plt.figure()
ax = fig2.add_subplot()
ax.plot(x_exp, y_exp, 'ro')
ax.set_xlabel("x", fontsize=14)
ax.set_ylabel("y", fontsize=14)
ax.plot(x_exp, exponential(x_exp, *popt), 'k',
        label="y= %0.2f( %0.2f^x) + (%0.2f)" % (popt[0], popt[1], popt[2]))
ax.legend(loc='best')
fig2.show()


x_natexp = np.linspace(1, 10, 50)
y_natexp = 3*(np.exp(3*x_natexp))+10
y_natexp_noise = 0.1*(np.random.normal(len(x_natexp)))
y_natexp += y_natexp_noise

popt, pcov = curve_fit(natural_exp, x_natexp, y_natexp)

fig3 = plt.figure()
ax = fig3.add_subplot()
ax.plot(x_natexp, y_natexp, 'ro')
ax.set_xlabel("x", fontsize=14)
ax.set_ylabel("y", fontsize=14)
ax.plot(x_natexp, natural_exp(x_natexp, *popt), 'k',
        label="y= %0.2f( e^ %0.2fx) + (%0.2f)" % (popt[0], popt[1], popt[2]))
ax.legend(loc='best')
fig3.show()
