import sys
from directory import *

if len(sys.argv) == 1:
    print Help().assist()

elif len(sys.argv) == 2:
    if sys.argv[1] == "--help":
        print Help().assist()
    elif sys.argv[1] == "list":
        print SolarHelper().getPlanetsSortedAlphabetically()
    else:
        print Help().assist()
elif len(sys.argv) == 3:
    if sys.argv[1] == "planet":
        SolarHelper().getPlanetFactsAndCompisition(sys.argv[2])
    else:
        print Help().assist()
elif len(sys.argv) == 4:
    if sys.argv[1] == "list":
        if sys.argv[2] == "-orderby":
            if sys.argv[3] == "mass":
                print SolarHelper().getPlanetsSortedByMass()
            elif sys.argv[3] == "diameter":
                print SolarHelper().getPlanetsSortedByDiameter()
            else:
                print Help().assist()
        else:
            print Help().assist()
    else:
        print Help().assist()
else:
    print Help().assist()
