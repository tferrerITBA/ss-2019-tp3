from parser import parseDirectoryFromArgs
from calculator import calculateDistance, squareList, averageLists, linearRegression, calculateDeltas, average, discreteRange, PDF
from functools import reduce #python 3

def getBallDistancesFromOrigin(simulation):
  firstBall = simulation.steps[0].ball
  distances = [calculateDistance(firstBall.position(), step.ball.position()) for step in simulation.getSecondHalf()]
  return distances

# Not used yet
def getParticleDistancesFromOrigin(simulation, index = 5):
  firstParticle = simulation.steps[0].particles[index]
  distances = [calculateDistance(firstParticle.position(), step.particles[index].position()) for step in simulation.steps]
  return distances

def calculateCollisionFrequency(simulation):
  amountOfCollisions = len(simulation.steps)
  totalSimulationTime = simulation.steps[-1].time
  return amountOfCollisions/totalSimulationTime

def calculateCollisionTimesAverage(simulation):
  accumulatedTimes = [step.time for step in simulation.steps]
  deltaTimes = calculateDeltas(accumulatedTimes)
  return average(deltaTimes)

def calculateProbabilityCollisionTimesDistribution(simulation):
  accumulatedTimes = [step.time for step in simulation.steps]
  deltaTimes = calculateDeltas(accumulatedTimes)
  hist, bin_edges = PDF(deltaTimes, 0.25)
  return hist * calculateDeltas(bin_edges)

def calculateProbabilityVelocities(simulation):
  lastThirdSteps = simulation.getLastThird()
  listOfSpeeds = [step.getParticlesSpeed() for step in lastThirdSteps]
  speeds = reduce(lambda x,y: x+y,listOfSpeeds)
  hist, bin_edges = PDF(speeds, 0.2)
  print(bin_edges)
  return hist * calculateDeltas(bin_edges)

def calculateDiffusion(simulations, getDistanceFromOrigin = getBallDistancesFromOrigin):
  squaredDistances = [squareList(getDistanceFromOrigin(simulation)) for simulation in simulations]
  averageSquaredDistances = averageLists(squaredDistances)
  diffusion = linearRegression(averageSquaredDistances)
  return diffusion

simulations = parseDirectoryFromArgs()
print(calculateDiffusion(simulations))