import numpy

# Calculate euclidean distance between two points
def calculateDistance(a, b):
  a = numpy.array(a)
  b = numpy.array(b)
  return numpy.linalg.norm(a-b)

# Takes a list and returns a new list with the first list's elements squared
def squareList(lst):
  return [x ** 2 for x in lst]

# Takes a list and returns a list of the differences between the elements
# e.g. [1,2,4,5] = [1,2,1]
def calculateDeltas(lst):
  return [ abs(element) for element in numpy.diff(lst)]

# Takes multiple lists, and returns a single list where each element is the average of the elements
# of the passed list in a specific index
def averageLists(lists):
  return numpy.mean(numpy.array([ i for i in lists]), axis=0 )

# Returns the average of a list
def average(lst):
  return numpy.mean(lst)

def discreteRange(*args):
  return numpy.arange(*args)

def PDF(lst, maxValue):
  return numpy.histogram(lst, bins=10, range=(0, maxValue), density=True)

# Returns a linear regresion (slope) from a list of points
def linearRegression(data):
  m,b = numpy.polyfit(range(len(data)), data, 1)
  return m