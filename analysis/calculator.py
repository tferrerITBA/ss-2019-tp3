import numpy

# Calculate euclidean distance between two points
def calculateDistance(a, b):
  a = numpy.array(a)
  b = numpy.array(b)
  return numpy.linalg.norm(a-b)

# Takes a list and returns a new list with the first list's elements squared
def squareList(lst):
  return [x ** 2 for x in lst]

# Takes multiple lists, and returns a single list where each element is the average of the elements
# of the passed list in a specific index
def averageLists(lists):
  return numpy.mean(numpy.array([ i for i in lists]), axis=0 )

# Returns a linear regresion (slope and b) from a list of points
def linearRegression(data):
  m,b = np.polyfit(range(len(data)), data, 1)
  return [m, b]