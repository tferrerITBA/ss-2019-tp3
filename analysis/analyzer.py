from parser import parseDirectoryFromArgs
from calculator import calculateDistance, squareList, averageLists, linearRegression, calculateDeltas, average, discreteRange, PDF

def getBallDistancesFromOrigin(simulation):
  firstBall = simulation.steps[0].ball
  distances = [calculateDistance(firstBall.position(), step.ball.position()) for step in simulation.steps.getSecondHalf()]
  return distances

# Not used yet
def getParticleDistancesFromOrigin(simulation, index = 5):
  firstParticle = simulation.steps[0].particles[index]
  distances = [calculateDistance(firstParticle.position(), step.particles[index].position()) for step in simulation.steps]
  return distances

def calculateCollisionFrequency(simulation):
  amountOfCollisions = len(simulation.steps)
  totalSimualtionTime = simulation.steps[-1].time
  return amountOfCollisions/totalSimualtionTime

def calculateCollisionTimesAverage(simulation):
  accumulatedTimes = [step.time for step in simulation.steps]
  deltaTimes = calculateDeltas(accumulatedTimes)
  return average(deltaTimes)

def calculateProbabilityCollisionTimesDistribution(simulation):
  accumulatedTimes = [step.time for step in simulation.steps]
  deltaTimes = calculateDeltas(accumulatedTimes)
  hist, bin_edges = PDF(deltaTimes, 0.5)
  return hist


def calculateDiffusion(simulations, getDistanceFromOrigin = getBallDistancesFromOrigin):
  squaredDistances = [squareList(getDistanceFromOrigin(simulation)) for simulation in simulations]
  averageSquaredDistances = averageLists(squaredDistances)
  print(squaredDistances)
  diffusion = linearRegression(averageSquaredDistances)
  return diffusion

simulations = parseDirectoryFromArgs()
print(calculateDiffusion(simulations))