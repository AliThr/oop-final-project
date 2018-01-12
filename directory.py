
class Planet():
    """This class defines the different variables to be initiated one every planet."""
    def __init__(self, planet_name, planet_mass, planet_distanceFromSun, planet_funFact, planet_diameter, number_of_moons, orbitalPeriod):
        self.name = planet_name
        self.mass = planet_mass
        self.distanceFromSun = planet_distanceFromSun
        self.funFact = planet_funFact
        self.diameter = planet_diameter
        self.moons = number_of_moons
        self.orbitalPeriod = orbitalPeriod

class Jovian(Planet):
    def __init__(self, planet_name, planet_mass, planet_distanceFromSun, planet_funFact, planet_diameter, number_of_moons, orbitalPeriod, composition):
        Planet.__init__(self, planet_name, planet_mass, planet_distanceFromSun, planet_funFact, planet_diameter, number_of_moons, orbitalPeriod)
        self.composition = composition

class Terrestrial(Planet):
    def __init__(self, planet_name, planet_mass, planet_distanceFromSun, planet_funFact, planet_diameter, number_of_moons, orbitalPeriod, composition):
        Planet.__init__(self, planet_name, planet_mass, planet_distanceFromSun, planet_funFact, planet_diameter, number_of_moons, orbitalPeriod)
        self.composition = composition



class Star():
    """This class defines the different variables to be initiated one every planet."""
    def __init__(self, star_name, star_mass, star_escape_velocity, star_diameter, star_fun_fact, star_surface_temp, star_core_temp):
        self.name = star_name
        self.mass = star_mass
        self.escapeVelocity = star_escape_velocity
        self.diameter = star_diameter
        self.funFact = star_fun_fact
        self.surfaceTemp = star_surface_temp
        self.coreTemp = star_core_temp
'''
class Composition(Planet):
    """This class takes the composition of a planet, defined in the class 'Planet', and determines whether it is composed mainly of rock or gas."""
    def __init__(self, planet_name, planet_mass, planet_composition, planet_distanceFromSun, planet_funFact, planet_diameter, number_of_moons, orbitalPeriod):
        def getComposition(self):
            if planet_composition == "terrestrial":
                return "This planet is a rocky body."
            elif planet_composition == "jovian":
                if planet_name == "Jupiter" or planet_name == "Saturn":
                    return "This planet is a gaseous body."
                elif planet_name == "Neptune" or planet_name == "Uranus":
                    return "This planet is an icy and gaseous body."
'''
'''
class solarHelper():
    """This class contains all functions that are called within 'solarsystem.py'."""
    def assist():
        return """To order the planets alphabetically:    solarsystem.py list \nTo order the planets by mass (highest to lowest):   solarsystem.py list -orderby mass \nTo order the planets by diameter:   solarsystem.py list -orderby diameter"""
    def alphabetically():
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

    def massSort():
        for i in planets:
            newPlanets.append(i.mass)
        newPlanetsMass = sorted(newPlanets, reverse=True)
        for i in newPlanetsMass:
            for j in planets:
                if j.mass == i:
                    planetsMass.append(j.name)
        return planetsMass
    def diaSort():
        for i in planets:
            newPlanets.append(i.diameter)
        newPlanetsMass = sorted(newPlanets, reverse=True)
        for i in newPlanetsMass:
            for j in planets:
                if j.diameter == i:
                    planetsDiameter.append(j.name)
        return planetsDiameter
'''
