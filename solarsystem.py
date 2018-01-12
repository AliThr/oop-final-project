import sys
from solarCompiler import *
from directory import *

def assist():
    return """To order the planets alphabetically:    solarsystem.py list \nTo order the planets by mass (highest to lowest):   solarsystem.py list -orderby mass \nTo order the planets by diameter:   solarsystem.py list -orderby diameter"""
def alphabetically():
    print "A list of the planets in the solar system, sorted alphabetically: "
    print "---"
    for i in planets:
        newPlanets.append(i.name)
    return sorted(newPlanets)
def factAndComp():
    usrInp = sys.argv[2].lower()
    for planet in planets:
        if planet.name.lower() == usrInp:
            print planet.name + ":"
            print "---"
            print "Fun fact: " + planet.funFact
            print "---"
            print "The composition of this planet is primarily " + planet.composition
            print "---"
            print "The diameter of " + planet.name + " is " + str(planet.diameter / 1000.0) + " thousand km."
            print "---"
            print "The distance of " + planet.name + " from the Sun is " + str(planet.distanceFromSun / 1000000) + " million km."
        else:
            return "That is not a valid planet"

def massSort():
    print "A list of the planets in the solar system, sorted by mass, from largest to smallest: "
    print "---"
    for i in planets:
        newPlanets.append(i.mass)
    newPlanetsMass = sorted(newPlanets, reverse=True)
    for i in newPlanetsMass:
        for j in planets:
            if j.mass == i:
                planetsMass.append(j.name)
    return planetsMass
def diaSort():
    print "A list of the planets in the solar system, sorted by their diameter, from largest to smallest: "
    print "---"
    for i in planets:
        newPlanets.append(i.diameter)
    newPlanetsMass = sorted(newPlanets, reverse=True)
    for i in newPlanetsMass:
        for j in planets:
            if j.diameter == i:
                planetsDiameter.append(j.name)
    return planetsDiameter
if len(sys.argv) == 1:
    print assist()

elif len(sys.argv) == 2:
    if sys.argv[1] == "--help":
        print assist()
    elif sys.argv[1] == "list":
        print alphabetically()
    else:
        print assist()
elif len(sys.argv) == 3:
    if sys.argv[1] == "planet":
        print factAndComp()
    else:
        print assist()
elif len(sys.argv) == 4:
    if sys.argv[1] == "list":
        if sys.argv[2] == "-orderby":
            if sys.argv[3] == "mass":
                print massSort()
            elif sys.argv[3] == "diameter":
                print diaSort()
            else:
                print assist()
        else:
            print assist()
    else:
        print assist()
else:
    print assist()
'''
if len(sys.argv) == 1:
    print 'help'
elif len(sys.argv) == 2:
    if sys.argv[1] == '--help':
        print 'help'
    elif sys.argv[1] == 'list':
        print 'list'
    else:
        print 'help'
elif len(sys.argv) == 3:
    if sys.argv[1] == 'planet':
        if sys.argv[2] == 'planet':
            print 'Interesting info on <planet>, including its diameter, mass, distance from sun and composition.'
        else:
            print 'help here'
    else:
        print 'help'
elif len(sys.argv) == 4:
    if sys.argv[1] == 'list':
        if sys.argv[2] == '-orderby':
            if sys.argv[3] == 'mass':
                print 'List of Planets in order of mass, largest to smallest.'
            elif sys.argv[3] == 'diameter':
                print 'List of Planets in order of diameter, largest to smallest.'
            else:
                print 'help here'
        else:
            print 'help here'
    else:
        print 'help here'
else:
    print 'help here'
'''