# astronomy.py 12.10.3

from math import *

G = 6.673e-11
c = 2.998e8
H = 80	# km/s/Mpc
v = 0
relg = 1/(sqrt(1-((v/c)**2)))

def gforce(m1, m2, r):
	''' (int, int, int) -> int
	
	Calculates gravitational force between masses m1 and m2 (kg) at a separation of r (m).
	'''
	
	global G
	return str((G*m1*m2)/(r**2)) + ' N'
	
def magabs(mapp, d):
	''' (number, number) -> float
	Return absolute magnitude given apparent magnitude and distance (parsecs), mapp and d.
	'''
	return str(5 + mapp - (5*math.log(d, 10)))

def magapp(mabs, d):
	''' (number, number) -> float
	Return apparent magnitude given absolute magnitude and distance (parsecs), mapp and d.
	'''
	return str((5*math.log(d) - 5) + M)
	
def luminosity(flux):
	''' (number) -> float
	Return luminosity of a star at a given distance d, considering its flux.
	'''
	return str(4*math.pi*(d**2)*flux) + ' W'
	
def schwradius(m):
	''' (number) -> float
	Return the Schwarzchild radius of an object of mass m
	'''
	global G
	global c
	return str((2*G*m)/(c**2)) + ' m'
	
def hubblevel(d):
	global H
	return str(H*d) + ' km/s/Mpc'

def hubbledis(v):
	global H
	return str(v/H) + ' km/s'

def specrelt(t):
	''' (number) -> float
	Return relativistic time when given stationary time.
	'''
	global relg
	return str(relg*t) + ' s'

def specrelm(m):
	''' Return relativistic mass. '''
	global relg
	return str(relg*m) + ' kg'

def specrelx(x):
	''' Return relativistic length.'''
	global relg
	return str(x/relg) + ' m'