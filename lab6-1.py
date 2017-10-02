
import math
class Distance:
	def __init__(self , x , y):
		self.x = x
		self.y = y
	def distance (self,other):
		dist = math.sqrt ((other.x - self.x) ** 2 + (other.y - self.y) ** 2)
		return dist

x = Distance(2 ,4)
y = Distance(5, 9)
print (str(x.distance(y)))

