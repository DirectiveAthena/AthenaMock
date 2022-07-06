# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
import random

# Custom Library
from AthenaLib.functions.random import random_bool

# Custom Packages
from AthenaMock.data.usernames.enclosing import ENCLOSING
from AthenaMock.data.usernames.names import NAMES
from AthenaMock.data.usernames.end import END
from AthenaMock.data.usernames.seperations import SEPARATIONS
from AthenaMock.functions.generators_seed import generate_random_seed

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------

def generate_username(*,seed=None):
    if seed is None:
        seed = generate_random_seed()

    # define and use the seed
    #   if a same seed is used, the same username will be generated
    random.seed(seed)

    enclose = random.choice(ENCLOSING) if random_bool(1/4) else ""

    name_partials = {random.choice(NAMES) for _ in range(random.randint(1, 5))}
    sep = random.choice(SEPARATIONS) if random_bool(1/10) else ""
    name = sep.join(
        name.capitalize() if random_bool() else name
        for name in name_partials
    )

    # decide if the username has to have some sort of end tag
    end = (
        "".join(str(random.randint(0,9)) for _ in range(random.randint(0, 5)))
        if random_bool(1/10) else random.choice(END)
    ) if random_bool(1/5) else ""

    return f"{enclose}{name}{enclose[::-1]}{end}"
