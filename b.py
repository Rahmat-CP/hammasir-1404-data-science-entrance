import random
from abc import ABC, abstractmethod

class MapError(Exception):
    
    pass

class Place(ABC):
    
    def __init__(self, name, x, y):
        self.__name = name
        self.__cordinate = (x, y)
        
    @property
    def name(self):
        return self.__name
    
    @property
    def cordinate(self):
        return self.__cordinate
    
    @abstractmethod
    def display(self):
        pass
    
class POI(Place):
    
    def __init__(self, name, x, y, category):
        super().__init__(name, x, y)
        self.__category = category
        
    @property
    def category(self):
        return self.__category
    
    def display(self):
        print(f'name: {self.name}, category: {self.category}, cordinate: {self.cordinate}')
        

class Map:
    
    def __init__(self):
        self.__pois = {}
        self.__routes = {}
        
    def add_poi(self, poi):
        
        if poi.name in self.__pois:
            raise MapError(f'Error: a Place of interests with the name {poi.name} already exist!')
        
        self.__pois[poi.name] = poi
        self.__routes[poi.name] = {}
        print(f'{poi.name} added to the map successfully!')
        
        
    def add_route(self, poi1, poi2):
        if poi1.name not in self.__pois or poi2.name not in self.__pois:
            raise MapError('Error: one of the place of interests does not exist in the map!')
        
        if poi1.name == poi2.name:
            raise MapError('Error: both places are the same!')
        
        weight = random.randint(1, 100)
        self.__routes[poi1.name][poi2.name] = weight
        self.__routes[poi2.name][poi1.name] = weight
        
        print(f'route added between {poi1.name} and {poi2.name} by weight {weight} successfully!')
        
    
    def display(self):
        print('\nplaces of interests:')
        if not self.__pois:
            print('no place of interests exist in the map!')
        else:
            for poi in self.__pois:
                self.__pois[poi].display()
                
        print('\nroutes of interests:')
        if not self.__routes:
            print('no routes of interests exist in the map!')
        else:
            for source, connection in self.__routes.items():
                for destination, weight in connection.items():
                    print(f'{source} [to] {destination} [by weight] {weight}')


if __name__ == "__main__":
    
    mp = Map()
    
    poi1 = POI('Haram', 32.5235, 42.2533, 'historic')
    poi2 = POI('Park Mellat', 56.4454, 89.4566, 'nature')
    poi3 = POI('Ferdowsi University', 45.4666, 10.4656, 'education')
    poi4 = POI('neshan company', 155.4655, 89.4654, 'comany')
    
    try:
        mp.add_poi(poi1)
        mp.add_poi(poi2)
        mp.add_poi(poi3)
        mp.add_poi(poi4)
    except MapError as e:
        print(e)
        
    try:
        mp.add_poi(poi1)
    except MapError as e:
        print(e) # this is work!
        
    try:
        mp.add_route(poi1, poi2)
        mp.add_route(poi1, poi3)
        mp.add_route(poi2, poi4)
    except MapError as e:
        print(e)
    
    
    try:
        mp.add_route(poi1, poi1)
    except MapError as e:
        print(e) # this is work!


    mp.display()