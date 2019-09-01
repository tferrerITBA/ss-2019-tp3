from parser import parseFile
from calculator import calculateDistance

def getDistancesFromOrigin(simulation):
  firstBall = simulation.steps[0].ball
  distances = [calculateDistance(firstBall.position(), step.ball.position()) for step in simulation.steps]
  return distances

simulation = parseFile('test.xyz')
getDistancesFromOrigin(simulation)