SciCal - Science Calculator
===========================
Copyright (c) 2012 Conor Farrell [conor.farrell8@gmail.com]
Released under GNU GPL3 (please see Section 6 and COPYING.md).

1. Introduction
---------------
SciCal is a work in progress, aimed at simplifying common (but sometimes long) calculations undertaken in science. At the moment, SciCal will work under python3, and from there the user can execute the imported modules and their functions. For example:

	>>> s.a.gforce(23,56,1200)
	5.968627777777778e-14

'a' denotes the 'astronomy.py' module (imported as 'a' for shorthand; 'physics.py' imports as 'p', etc.), and gforce(mass1, mass2, separation) is the function that calculates the gravitational force between two bodies.

Note that all calculations are done in the SI metric system, as all mathematics damn well should be!

2. Usage
--------
Download all files into the same directory. At the command line, run:

	~> python3
	>>> import scical as s

From there the user can run the necessary modules as listed below. To run the gforce() function in astronomy, for example, type:

	s.a.gforce(you numbers go here)

3. Modules
----------
3.1 astronomy.py

	a.gforce(mass1, mass2, separation)	Gravitational force between two masses
	a.magabs(magnitude, distance)				Absolute magnitude from apparent magnitude and distance
	a.magapp(magnitude, distance)				Apparent magnitude from absolute magnitude and distance
	a.luminosity(flux)									Luminosity given flux
	a.schwradius(mass)									Calculate Schwarzchild radius of a mass
	a.hubblevel(distance)								Calculate the velocity of a body given its distance using the Hubble relation
	a.hubbledis(velocity)								Calculate the distance of a body given its velocity using the Hubble relation
	a.specrelt(time)										Return relativistic time dt given t
	a.specrelm(mass)										Return relativistic time dm given m
	a.specrelx(length)									Return relativistic time dx given x

3.2 physics.py

	p.coulomb(charge1, charge2, distance)	Calculate force between two charges at a distance
	p.newton2(mass, acceleration)					Solve Newton's second law to give a force
	p.newton3(force)											Solve Newton's third law to give a force
	p.emc2(mass)													Return energy given mass
	p.phenergywav(wavlength)							Calculates photon energy from wavelength of the photon
	p.phenergyfreq(frequency)							Calculates photon energy from frequency of the photon
	decaylife(tau, n)											Return 1/n-life of a particle (i.e n=2 gives half-life, n=3 gives third-life, etc) given mean lifetime of particle before decay, tau

4. Development
--------------
Feel free to fork this project and expand on the modules as you see fit! Personally, I will focus on astronomy and physics modules for the moment, as they would form the bulk of calculations I would do. Modules can be written for anything that has standardised calculations: biology, chemistry, economics, accounting, engineering, etc etc.

5. To-Do List
-------------
- Allow the user to check what modules are loaded by scical.py.
- Round up numbers to certain number of decimal places by default; allow user to define number of places.

6. Licensing
------------
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.