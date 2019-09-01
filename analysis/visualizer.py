import numpy as np
import matplotlib.pyplot as plt

def generateChart()
  fig = plt.figure()
  x = np.arange(10)
  y = 2.5 * np.sin(x / 20 * np.pi)
  yerr = np.linspace(0.05, 0.2, 10)

  plt.errorbar(x, y + 3, yerr=yerr, label='both limits (default)')

  plt.legend(loc='lower right')
  plt.show()