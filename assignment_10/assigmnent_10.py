'https://www.youtube.com/watch?v=HTLu2DFOdTg&list=FLJpj9JO97RXNeiS1yV47URg&index=20&t=0s'

import math
from random import random, seed

class Circle(object):
	'An advanced circle analytic toolkit'

	__slots__ = ['diameter']
	version = '0.7'




	def __init__(self, radius):
		self.radius = radius

	@property
	def radius(self):
		'Radius of a circle'
		return self.diameter / 2.0

	@radius.setter
	def radius(self, radius):
		self.diameter = radius * 2.0

	def area(self):
		'Perform quadrature on a shape of uniform radius'
		p = self.__perimeter()
		r = p / math.pi / 2.0
		return math.pi * r ** 2.0


	def perimeter(self):
		return 2.0 * math.pi * self.radius

	def angle_to_grade(angle):
		'Convert angle in degree to a precentage grade'
		return math.tan(math.radians(angle)) * 100.0

	_perimeter = perimeter

	# Alternative constructor
	@classmethod
	def from_bbd(cls, bbd):
		'Construct a circle from a bounding box diagonal'
		radius = bbd / 2.0/ math.sqrt(2.0)
		return Circle(radius)

	__perimeter = perimeter



# Tutorial ------------------------------------------

print('Circuituous version', Circle.version)
c = Circle(10)
print('A circle of radius', c.radius)
print('has an area of', c.area())
print('')


# Academia ------------------------------------------

n = 10000000

seed(8675309)
print('Using Circuituous(tm) version', Circle.version)
circles = [Circle(random()) for i in range(n)]
print('The average area of', n, 'random circles')
avg = sum([c.area() for c in circles ]) / n
print('is %.1f' % avg)
print('')


# Rubber sheet company ------------------------------------------

cuts = [0.1, 0.7, 0.8]
circles = [Circle(r) for r in cuts]
for c in circles:
	print('A circlet with with a radius of', c.radius)
	print('has a perimeter of', c.perimeter())
	print('and a cold area of', c.area())
	c.radius *= 1.1
	print('and a warm area of', c.area())
	print('')


# National tire chain ------------------------------------------

class Tire(Circle):
	'Tires are circles with a corrected perimeter'

	def perimeter(self):
		'Circumference corrected for the rubber'
		return Circle.perimeter(self) * 1.25

t = Tire.from_bbd(45)
print('A tire of radius', t.radius)
print('has an inner area of', t.area())
print('and an odometer corrected perimeter of', t.perimeter())
print('')


# National graphics company ------------------------------------------

"""bbd = 22.1
c = Circle(bbd_to_radius(bbd))
print('A circle with a bbd of 25.1')
print('has a radius of,' c.radius)
print('an an area of', c.area())"""
