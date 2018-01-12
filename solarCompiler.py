import directory
import argparse 
import operator
#   (self, planet_name, planet_mass, planet_compisition, planet_distanceFromSun, planet_funFact, planet_diameter, number_of_moons, orbitalPeriod)

#  def __init__(self, star_name, star_mass, star_escape_velocity, star_diameter, star_fun_fact, star_surface_temp, star_core_temp):
sun = directory.Star("Sun", 1.989 * 10**30, 617.7, 1391400, "some information will be added", 5778, 15000000)

mercury = directory.Terrestrial("Mercury", 3.285 * (10**23), 57910000, "Mercury, despite being the closest planet to the sun by quite a margin, is not actually the planet with the highest surface temperature, as it has no atmosphere to keep the heat in. That award goes to Venus, which is 467 C, 40 C hotter than Mercury.", 4879, 0, 88, "rock")
venus = directory.Terrestrial("Venus", 4.867 * (10**24), 108200000, "Due to the fact that Venus's rotation is retrograde (the opposite direction to which it orbits the sun) and it rotates very slowly, a day on the planet lasts longer than a it's year. It takes 225 Earth-days to orbit the sun but 243 Earth-days to complete a single rotation.", 12104, 0, 225, "rock")
earth = directory.Terrestrial("Earth", 5.972 * (10**24), 149600000, "Earth... is here!", 12742, 1, 365.25, "rock")
mars = directory.Terrestrial("Mars", 6.39 * (10**23), 227900000, "some information will be added", 6779, 2, 687, "rock")
jupiter = directory.Jovian("Jupiter", 1.898 * (10**27), 778500000, "some information will be added", 69911, 69, 4332.59, "gas")
saturn = directory.Jovian("Saturn", 5.683 * (10**26), 1429000000, "some information will be added", 58232, 62, 10759.22, "gas")
uranus = directory.Jovian("Uranus", 3.285 * (10**26), 2871000000, "some information will be added", 50274, 27, 30685, "gas")
neptune = directory.Jovian("Neptune", 1.024 * (10**26), 4498000000, "some information will be added", 49244, 14, 60182, "gas")

planets = [mercury, venus, earth, mars, jupiter, saturn, uranus, neptune]
planetsMass = []
planetsDiameter = []
newPlanets = []
'''
print newPlanets
for planet in planets:
        if planet.name.lower() == usrInp:
            return planet.funFact
'''

