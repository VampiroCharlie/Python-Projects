# This progarm is a "Class" with informaion on different cat breeds.

class Cat(object):# Cat Class 
    def __init__(self, breed, animal_kingdom, origin):# values in function
      self.self = self
      self.breed = breed
      self.animal_kingdom = animal_kingdom
      self.origin = origin

'''Information about different cats breeds below'''

abyssinian = Cat("Abyssinian", "Animalia", "Egypt")
american_bobtail = Cat("American Bobtail", "Animalia", "USA")
american_curl = Cat("American Curl", "Animalia", "USA")
american_shorthair = Cat("American Shorthair", "Animalia", "USA")
american_wirehair = Cat("American Wirehair", "Animalia", "USA")
balinese = Cat("Balinese", "Animalia", "USA")
bengal = Cat("Bengal", "Animalia", "India")
birman = Cat("Birman", "Animalia", "France")
bombay = Cat("Bombay", "Animalia", "USA")
british_shorthair = Cat("British Shorthair", "Animalia", "Great Britan")
burmese = Cat("Burmese", "Animalia", "Thailand")

'''print out values of begal cat'''
print (bengal.breed)# prints out breed of bengal cat
print (bengal.animal_kingdom)# prints out animal kingdom of bengal cat
print (bengal.origin)# prints out place of origin of bengal cat
