# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
import unittest
import timeit

# Custom Library
from AthenaMock.passwords.functions.generators import generate_password

# Custom Packages


# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
class TestGeneratePassword(unittest.TestCase):
    def test_general(self):
        password_generator = (generate_password(
                # seed="a"
            ) for _ in range(1_000))

        print(timeit.timeit(lambda :list(password_generator)))
        # print(*password_generator, sep="\n")