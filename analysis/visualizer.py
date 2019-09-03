import numpy as np
import matplotlib.pyplot as plt
from analyzer import calculateCollisionFrequency, calculateCollisionTimesAverage, calculateProbabilityCollisionTimesDistribution, calculateProbabilityVelocities
from parser import parseDirectoryFromArgs
import os

OUTPUT_FOLDER = 'output'
simulations = parseDirectoryFromArgs()

def saveFig(fig, name):
  if not os.path.exists(OUTPUT_FOLDER):
    os.makedirs(OUTPUT_FOLDER)
  fig.savefig(f'{OUTPUT_FOLDER}/{name}.png')
  
def ex3_1():
  for simulation in simulations:
    print(f'Simulacion: {simulation.name}')
    print(f'Frecuencia de colisiones (#/s):  {calculateCollisionFrequency(simulation)}')
    print(f'Promedio de tiempos de colision:  {calculateCollisionTimesAverage(simulation)}')
    times = calculateProbabilityCollisionTimesDistribution(simulation)

    fig, ax = plt.subplots()
    ax.hist(times, density=True, bins=100) 
    ax.set_xlabel('Tiempos de colisión (s)')
    ax.set_ylabel('Densidad de probabilidad')
    ax.set_title(f'Movimiento Browniano (N={len(simulation.steps[0].particles)})') 
    fig.tight_layout()
    saveFig(fig, f'{simulation.name}--3_1')

def ex3_2():
  for simulation in simulations:
    print(f'Simulacion: {simulation.name}')
    speeds, listOfSpeedsTime0 = calculateProbabilityVelocities(simulation)

    # grafica el ultimo tercio
    fig, ax = plt.subplots()
    ax.hist(speeds, density=True, bins=100) 
    ax.set_xlabel('Modulo de las velocidades (m/s)')
    ax.set_ylabel('Densidad de probabilidad')
    ax.set_title(f'Movimiento Browniano (N={len(simulation.steps[0].particles)}) - Ultimo tercio de tiempo') 
    fig.tight_layout()
    saveFig(fig, f'{simulation.name}--3_2')
    
    # grafica en t=0
    fig, ax = plt.subplots()
    ax.hist(listOfSpeedsTime0, density=True, bins=100) 
    ax.set_xlabel('Modulo de las velocidades (m/s)')
    ax.set_ylabel('Densidad de probabilidad')
    ax.set_title(f'Movimiento Browniano (N={len(simulation.steps[0].particles)}) - t=0') 
    fig.tight_layout()
    saveFig(fig, f'{simulation.name}--3_2--initial')

def ex3_3():
  diffusionSlope, diffusionB, averageSquaredDistances = calculateDiffusion()
  print(f'Coeficiente de difusion aproximado: {diffusionSlope}')