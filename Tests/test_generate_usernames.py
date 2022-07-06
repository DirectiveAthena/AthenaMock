# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
import unittest
import timeit

# Custom Library
from AthenaMock.functions.generator import generate_username

# Custom Packages


# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
class TestGenerateUsernames(unittest.TestCase):
    def test_general(self):
        username_generator = (generate_username(
                # seed="a"
            ) for _ in range(1_000_000))

        print(timeit.timeit(lambda :list(username_generator)))
        # print(*username_generator, sep="\n")
        # print(
        #
        # )