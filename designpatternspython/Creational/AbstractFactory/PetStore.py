class PetStore:
    """PetStore houses our Abstract Factory"""

    def __init__(self, pet_factory = None):
        """pet_factory is our Abstract Factory"""
        self._pet_factory = pet_factory

    def show_pet(self):
        """Utility method to print details of the objects"""

        pet = self._pet_factory.get_pet()
        pet_food = self._pet_factory.get_food()

        print("Our pet is a '{}' and his name is '{}'".format(pet, pet._name))
        print("Our pet says hello by '{}'".format(pet.speak()))
        print("Its food is '{}'".format(pet_food))