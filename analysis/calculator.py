import numpy

# Calculate euclidean distance between two points
def calculateDistance(a, b):
  a = numpy.array(a)
  b = numpy.array(b)
  return numpy.linalg.norm(a-b)

def squareList(lst):
  return [x ** 2 for x in lst]

def averageLists(lists):
  return numpy.mean(numpy.array([ i for i in lists]), axis=0 )

def linearRegression(data):
  m,b = np.polyfit(range(len(data)), data, 1)
  return [m, b]