from parser import parseDirectoryFromArgs
from calculator import calculateDistance, squareList, averageLists, linearRegression

def getBallDistancesFromOrigin(simulation):
  firstBall = simulation.steps[0].ball
  distances = [calculateDistance(firstBall.position(), step.ball.position()) for step in simulation.steps]
  return distances

def getParticleDistancesFromOrigin(simulation, index = 5):
  firstParticle = simulation.steps[0].particles[index]
  distances = [calculateDistance(firstParticle.position(), step.particles[index].position()) for step in simulation.steps]
  return distances

def calculateDiffusion(simulations, getDistanceFromOrigin = getBallDistancesFromOrigin):
  squaredDistances = [squareList(getDistanceFromOrigin(simulation)) for simulation in simulations]
  averageSquaredDistances = averageLists(squaredDistances)
  print(squaredDistances)
  diffusion = linearRegression(averageSquaredDistances)
  return diffusion

simulations = parseDirectoryFromArgs()
print(calculateDiffusion(simulations))