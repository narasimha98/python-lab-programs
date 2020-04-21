#Create a class to represent city which contains a list of places to see.
#   Provide methods to create the object with just the city name or with city name and places (stored as list)
#   Provide methods to add a place of visit, to remove place of visit, to display all places of visit.
#   Add exceptional handling so that remove does not crash if the given place is not in the city

class Place:
    def __init__(self, city, *places):
        self.city = city
        self.places = list(places)

    def add(self, place):
        self.places.append(place)

    def remove(self, place):
        # exception not checked
        self.places.remove(place)

    def disp(self):
        print(self.city)
        for place in self.places:
            print("\t", place)


p = Place('mysore', 'chamundi hills', 'zoo')
p.disp()
p.add('krs')
p.disp()
p.remove('zoo')
p.disp()



