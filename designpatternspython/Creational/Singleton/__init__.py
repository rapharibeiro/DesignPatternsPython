

from email.policy import HTTP
from tokenize import Single
from .Singleton import Singleton

def run():
    obj = Singleton(HTTP = "Hyper Text Transf Protocol")
    print(obj)
    obj2 = Singleton(SMTP = "Simple Main Transf Protocol")
    print(obj2)