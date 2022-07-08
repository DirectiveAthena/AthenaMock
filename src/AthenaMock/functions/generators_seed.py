# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
import os
import base64
from typing import Any
import random

# Custom Library

# Custom Packages

# ----------------------------------------------------------------------------------------------------------------------
# - Support Code -
# ----------------------------------------------------------------------------------------------------------------------
CONVERT_SEED = {
    bytes:lambda rand:rand,
    str:lambda rand: base64.b64encode(rand).decode("utf_8"),
    int:lambda rand: int(str(int(base64.b64encode(rand).hex(), 16)))
}

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
def generate_random_seed(length:int=64, result_type=str):
    return CONVERT_SEED[result_type](os.urandom(length))


def set_seed(seed:Any):
    # if the seed is undefined, generate a random one
    if seed is None:
        seed = generate_random_seed()
    # define and use the seed
    #   if a same seed is used, the same username will be generated
    random.seed(seed)
