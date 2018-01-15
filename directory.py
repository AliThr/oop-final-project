

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
    def __init__(self, planet_name, planet_mass, planet_distanceFromSun, planet_funFact, planet_diameter, number_of_moons, orbitalPeriod):
        Planet.__init__(self, planet_name, planet_mass, planet_distanceFromSun, planet_funFact, planet_diameter, number_of_moons, orbitalPeriod)
        self.composition = 'gas'

class Terrestrial(Planet):
    def __init__(self, planet_name, planet_mass, planet_distanceFromSun, planet_funFact, planet_diameter, number_of_moons, orbitalPeriod):
        Planet.__init__(self, planet_name, planet_mass, planet_distanceFromSun, planet_funFact, planet_diameter, number_of_moons, orbitalPeriod)
        self.composition = 'rock'

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


class Help():
    def __init__(self):
        pass
    
    def assist(self):
        return """To order the planets alphabetically:    solarsystem.py list \n
    To order the planets by mass (highest to lowest):   solarsystem.py list -orderby mass \n
    To order the planets by diameter (highest to lowest):   solarsystem.py list -orderby diameter \n
    To print details and an interesting fact about an individual planet: solarsystem.py planet <insert planet name>"""


class SolarHelper():
    """This class contains all functions that are called within 'solarsystem.py'."""
    def __init__(self):
        pass
    
    mercury = Terrestrial("Mercury", 3.285 * (10**23), 57910000, "Mercury, despite being the closest planet to the sun by quite a margin, is not actually the planet with the highest surface temperature, as it has no atmosphere to keep the heat in. That award goes to Venus, which is 467 C, 40 C hotter than Mercury.", 4879, 0, 88)
    venus = Terrestrial("Venus", 4.867 * (10**24), 108200000, "Due to the fact that Venus's rotation is retrograde (the opposite direction to which it orbits the sun) and it rotates very slowly, a day on the planet lasts longer than a it's year. It takes 225 Earth-days to orbit the sun but 243 Earth-days to complete a single rotation.", 12104, 0, 225)
    earth = Terrestrial("Earth", 5.972 * (10**24), 149600000, "Earth... is here!", 12742, 1, 365.25)
    mars = Terrestrial("Mars", 6.39 * (10**23), 227900000, "some information will be added", 6779, 2, 687)
    jupiter = Jovian("Jupiter", 1.898 * (10**27), 778500000, "Jupiter's red spot is a storm that is so large that it could fit the Earth inside of it, and it has been raging for at least 350 years. However, it is shrinking.", 69911, 69, 4332.59)
    saturn = Jovian("Saturn", 5.683 * (10**26), 1429000000, "Saturn is the only planet in the soslar system that is less dense (30% less) than water. That means that if you were able to find a large enough ocean, it would float!", 58232, 62, 10759.22)
    uranus = Jovian("Uranus", 3.285 * (10**26), 2871000000, "some information will be added", 50274, 27, 30685)
    neptune = Jovian("Neptune", 1.024 * (10**26), 4498000000, "some information will be added", 49244, 14, 60182)

    planets = [mercury, venus, earth, mars, jupiter, saturn, uranus, neptune]
    planetsMass = []
    planetsDiameter = []
    newPlanets = []

    def PrintPlanetsSortedAlphabetically(self):
        print "A list of the planets in the solar system, sorted alphabetically: "
        print "---"
        for i in self.planets:
            self.newPlanets.append(i.name)
        return sorted(self.newPlanets)


    def PrintPlanetFactsAndCompisition(self, planetName):
        usrInp = planetName.lower()
        for planet in self.planets:
            if planet.name.lower() == usrInp:
                print planet.name + ":"
                print "---"
                print "Fun fact: " + planet.funFact
                print "---"
                print "The composition of this planet is primarily " + planet.composition
                print "---"
                print "The diameter of " + planet.name + " is " + str(planet.diameter / 1000.0) + " thousand km."
                print "---"
                return "The distance of " + planet.name + " from the Sun is " + str(planet.distanceFromSun / 1000000) + " million km."
        return "That is not a valid planet"


    def PrintPlanetsSortedByMass(self):
        print "A list of the planets in the solar system, sorted by mass, from largest to smallest: "
        print "---"
        for i in self.planets:
            self.newPlanets.append(i.mass)
        newPlanetsMass = sorted(self.newPlanets, reverse=True)
        for i in newPlanetsMass:
            for j in self.planets:
                if j.mass == i:
                    self.planetsMass.append(j.name)
        return self.planetsMass


    def PrintPlanetsSortedByDiameter(self):
        print "A list of the planets in the solar system, sorted by their diameter, from largest to smallest: "
        print "---"
        for i in self.planets:
            self.newPlanets.append(i.diameter)
        newPlanetsMass = sorted(self.newPlanets, reverse=True)
        for i in newPlanetsMass:
            for j in self.planets:
                if j.diameter == i:
                    self.planetsDiameter.append(j.name)
        return self.planetsDiameter


