# physics.py 12.10.2

from math import *

ke = 8.987552e9
c = 2.998e8
planck = 6.626e-34

def coloumb(q1, q2, r):
	global ke
	return str((ke*q1*q2)/(r**2)) + ' N'
	
def newton2(m, a):
	return str(m*a) + ' N'
	
def newton3(force):
	return str(force * -1) + ' N'
	
def emc2(m)
	global c
	return str(m*(c**2)) + ' J'

def phenergywav(w)
	global planck
	return str((planck*c)/w) + ' J'
	
def phenergyfreq(f)
	global planck
	return str(planck*f) + ' J'
	
def decaylife(tau, n) # tau is mean lifetime of particle before decay
	''' (number, number) -> float
	Return the 1/n-life of a particle, i.e. n=2 gives half-life, n=3 gives third-life, etc.
	'''
	return str(tau*log(n)) + ' s (or appropriate unit as given in input)'