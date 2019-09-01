class Particle:
  def __init__(self, id, radius, mass, x, y, vx, vy):
    self.id = id
    self.radius = radius
    self.mass = mass
    self.x = x
    self.y = y
    self.vx = vx
    self.vy = vy
  def __str__(self):
    return f'Id: {self.id}\nRadius: {self.radius}\nMass: {self.mass}\nPosition X: {self.x}\nPosition Y: {self.y}\nVelocity X: {self.vx}\nVelocity Y: {self.vy}\n'

class Step:
  def __init__(self, time, particles):
    self.time = time
    self.particles = particles

class Simulation:
  def __init__(self, steps):
    self.steps = steps
