# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
import random
# Custom Library

# Custom Packages
from AthenaMock.data.text_choices import CHOICE_USERNAME

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
def generate_username(*,amount:int=24, length_min:int=4,length_max:int=16, choice:str=CHOICE_USERNAME,unique:bool=True):
    if unique:
        for username in _generate_username_unique(amount=amount, length_min=length_min, length_max=length_max, choice=choice):
            yield username
    else:
        for _ in range(amount):
         yield _generate_username_single(length_min=length_min, length_max=length_max, choice=choice)

def _generate_username_single(*, length_min:int=4,length_max:int=16, choice:str=CHOICE_USERNAME):
    return "".join(random.choice(choice) for _ in range(random.randint(length_min,length_max)))

def _generate_username_unique(*,amount:int=24, length_min:int=4,length_max:int=16, choice:str=CHOICE_USERNAME):
    mem:set[str] = set()
    while len(mem) <= amount:
        username = _generate_username_single(length_min=length_min, length_max=length_max, choice=choice)
        if username not in mem:
            mem.add(username)
            yield username



