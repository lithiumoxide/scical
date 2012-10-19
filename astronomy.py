import math

G = 6.673e-11
c = 3e8
H = 80	# km/s/Mpc

def gforce(m1, m2, r):
	''' (int, int, int) -> int
	
	Calculates gravitational force between masses m1 and m2 (kg) at a separation of r (m).
	'''
	
	global G
	return (G*m1*m2)/(r**2) + ' N'
	
def magabs(mapp, d)
	''' (number, number) -> float
	Return absolute magnitude given apparent magnitude and distance (parsecs), mapp and d.
	'''
	return 5 + mapp - (5*math.log(d))

def magapp(mabs, d)	
	''' (number, number) -> float
	Return apparent magnitude given absolute magnitude and distance (parsecs), mapp and d.
	'''
	return (5*math.log(d) - 5) + M
	
def luminosity(flux)
	''' (number) -> float
	Return luminosity of a star at a given distance d, considering its flux.
	'''
	return 4*math.pi*(d**2)*flux
	
def schwradius(m)
	''' (number) -> float
	Return the Schwarzchild radius of an object of mass m
	'''
	
	global G
	global c
	return (2*G*m)/(c**2) + ' m'
	
def hubblevel(d)
	global H
	return H*d + ' km/s/Mpc'

def hubbledis(v)
	global H
	return v/H + ' km/s'