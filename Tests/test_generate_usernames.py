# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
import unittest
import timeit

# Custom Library
from AthenaMock.functions.generators import generate_username

# Custom Packages


# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
class TestGenerateUsernames(unittest.TestCase):

    def _generate_usernames(self):
        for username in generate_username(
                amount=1_000,
                length_min=4,
                length_max=16
        ):
            yield username

    def _generate_usernames_write_to_file(self):
        with open("username.txt", "w+") as file:
            for username in self._generate_usernames():
                file.write(f"{username}\n")

    def test_general(self):
        print(
            timeit.timeit(
                lambda : self._generate_usernames()
            )
        )
        print(
            timeit.timeit(
                lambda : self._generate_usernames_write_to_file()
            )
        )