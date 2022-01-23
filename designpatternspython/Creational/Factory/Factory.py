from designpatternspython.Objects.Dog import Dog
from designpatternspython.Objects.Cat import Cat

def get_pet(pet="dog"): 

    "The factory method"

    pets = dict(dog=Dog("Hope"), cat=Cat("Peace"))

    return pets[pet]

def run():
    new_cat = get_pet("cat")
    print(new_cat.speak())