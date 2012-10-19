import math

G = 6.673e-11

def gforce(m1, m2, r):
	''' (int, int, int) -> int
	
	Calculates gravitational force between masses m1 and m2 (kg) at a separation of r (m).
	'''
	
	global G
	return (G*m1*m2)/(r**2)
	
	
G = 6.673e-11

def gforce(m1, m2, r):
	global G
	return (G*m1*m2)/(r**2)