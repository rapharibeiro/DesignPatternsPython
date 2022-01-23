from .DogFactory import DogFactory
from .CatFactory import CatFactory
from .PetStore import PetStore

def run():
    factory = DogFactory("Gaia")
    shop = PetStore(factory)    
    shop.show_pet()