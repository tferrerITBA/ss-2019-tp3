# Calculate euclidean distance between two points
def distanceFromOrigin(a, b):
  a = numpy.array(a)
  b = numpy.array(b)
  return numpy.linalg.norm(a-b)