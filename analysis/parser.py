from models import Particle, Step, Simulation

def parseFile(filename):
  lines = [line.rstrip('\n') for line in open(filename)]

  steps = []
  while len(lines) > 0:
    steps.append(parseStep(lines))
  
  return Simulation(steps)

def parseStep(lines):
  nextLines = int(lines.pop(0))
  time = float(lines.pop(0).split("Time=").pop())
  particles = [ parseParticle(lines.pop(0)) for _ in range(nextLines)]
  return Step(time, particles)

def parseParticle(line):
  properties = line.split(" ")
  particle = Particle(*properties)
  return particle