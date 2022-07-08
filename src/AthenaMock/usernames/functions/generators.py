# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
import random

# Custom Library
from AthenaLib.functions.random import random_bool
import AthenaLib.data.text as text

# Custom Packages
from AthenaMock.usernames.data.enclosing import ENCLOSING
from AthenaMock.usernames.data.names import NAMES, NAMES_ADJECTIVES
from AthenaMock.usernames.data.end import END
from AthenaMock.usernames.data.seperations import SEPARATIONS
from AthenaMock.data.colors import COLORS
from AthenaMock.data.animals import ANIMALS
from AthenaMock.data.names.first_names import FIRST_NAMES
from AthenaMock.data.names.sur_names import SUR_NAMES

from AthenaMock.functions.generators_seed import set_seed

from AthenaMock.usernames.models.username import Username

# ----------------------------------------------------------------------------------------------------------------------
# - Support Code -
# ----------------------------------------------------------------------------------------------------------------------
NAME_CHOICE = [*NAMES, *ANIMALS, *COLORS,*FIRST_NAMES,*SUR_NAMES]

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
def generate_username_2():
    # todo System like generate_username_1 but without the Object creation and only functional approach
    pass

def generate_username_1(
        seed=None,
        *,
        probability_separation:float =          1/5,
        probability_adjective:float =           1/2,
        probability_capitalize:float =          1/2,
        probability_end_number:float=           1/10,
        probability_enclosing:float=            1/4,
        probability_enclosing_no_start:float=   1/12,
        probability_enclosing_no_end:float=     1/12,
        **_
) -> str:
    # if the seed is undefined, generate a random one
    #   The function below will also invoke the random.seed(seed) so the seed is set
    set_seed(seed)

    return str(
        Username()
        .numerical_end(random_bool(probability_end_number))
        .enclosing(
            random.choice(ENCLOSING) if random_bool(probability_enclosing) else text.NOTHING,
            start=random_bool(probability_enclosing_no_start),
            end=random_bool(probability_enclosing_no_end)
        )
        .name(
            (random.choice(SEPARATIONS) if random_bool(probability_separation) else text.NOTHING).join(
                name.capitalize() if random_bool(probability_capitalize) else name
                for name in {random.choice(NAME_CHOICE) for _ in range(random.randint(2, 3))}
            ),
        )
        .adjective(
            random.choice(NAMES_ADJECTIVES) if random_bool(probability_adjective) else text.NOTHING
        )
    )


# ----------------------------------------------------------------------------------------------------------------------
def generate_username_0(
        seed=None,
        *,
        probability_separation:float =          1/5,
        probability_adjective:float =           1/2,
        probability_capitalize:float =          1/2,
        probability_end:float=                  1/5,
        probability_end_number:float=           1/10,
        probability_enclosing:float=            1/4,
        probability_enclosing_no_start:float=   1/12,
        probability_enclosing_no_end:float=     1/12,
        **_
):
    # if the seed is undefined, generate a random one
    #   The function below will also invoke the random.seed(seed) so the seed is set
    set_seed(seed)

    #generate the bare name
    sep = random.choice(SEPARATIONS) if random_bool(probability_separation) else ""
    name = sep.join(
        name.capitalize() if random_bool(probability_capitalize) else name
        for name in {random.choice(NAME_CHOICE) for _ in range(random.randint(1, 3))}
    )

    # add a random adjective in front 1/2 chance by default
    adjective =  random.choice(NAMES_ADJECTIVES) if random_bool(probability_adjective) else ""

    # decide if the username has to have some sort of end partial
    end = (
        "".join(str(random.randint(0,9)) for _ in range(random.randint(0, 5)))
        if random_bool(probability_end_number) else random.choice(END)
    ) if random_bool(probability_end) else ""

    # decide if the enclosing will be present or not
    #   Also has a specific chance not to generate one side at all
    enclose = random.choice(ENCLOSING) if random_bool(probability_enclosing) else ""
    enclose_start = "" if random_bool(probability_enclosing_no_start) else enclose
    enclose_end = "" if random_bool(probability_enclosing_no_end) else enclose[::-1]

    # return the name fully assembled
    return f"{enclose_start}{adjective}{name}{enclose_end}{end}"
