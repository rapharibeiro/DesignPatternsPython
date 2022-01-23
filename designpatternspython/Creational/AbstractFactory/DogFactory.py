from designpatternspython.Objects.Dog import Dog

class DogFactory:
    """Concrete Factory"""

    def __init__(self, name):
        self._name = name

    def get_pet(self):
        """Returns a Dog object"""
        return Dog(self._name)

    def get_food(self):
        """Returns a Dog Food object"""
        return "Dog Food"