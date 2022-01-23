from designpatternspython.Objects.Cat import Cat

class CatFactory:
    """Concrete Factory"""

    def __init__(self, name):
        self._name = name

    def get_pet(self):
        """Returns a Cat object"""
        return Cat(self._name)

    def get_food(self):
        """Returns a Cat Food object"""
        return "Cat Food"