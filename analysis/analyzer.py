from parser import parseFile
from calculator import calculateDistance, squareList, averageLists, linearRegression

def getDistancesFromOrigin(simulation):
  firstBall = simulation.steps[0].ball
  distances = [calculateDistance(firstBall.position(), step.ball.position()) for step in simulation.steps]
  return distances

def calculateDiffusion(simulations):
  squaredDistances = [squareList(getDistancesFromOrigin(simulation)) for simulation in simulations]
  averageSquaredDistances = averageLists(squaredDistances)
  [diffusion] = linearRegression(averageSquaredDistances)
  return diffusion

simulation = parseFile('test.xyz')
getDistancesFromOrigin(simulation)