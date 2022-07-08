# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
import random
import string

# Custom Library

# Custom Packages

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
class Username:
    _numerical_end:str
    _numerical_end_enabled:bool
    _enclosing:str
    _enclosing_start:bool
    _enclosing_end:bool
    _name:str
    _adjective:str
    __slots__ = ("_numerical_end","_enclosing", "_name", "_enclosing_start", "_enclosing_end",
                 "_numerical_end_enabled", "_adjective")


    def numerical_end(self, enabled:bool) -> Username:
        self._numerical_end_enabled = enabled
        if self._numerical_end_enabled:
            self._numerical_end = "".join(random.choice(string.digits) for _ in range(random.randint(1,5)))
        return self

    def enclosing(self, enclosing:str, start:bool, end:bool) -> Username:
        self._enclosing = enclosing
        self._enclosing_start = not start
        self._enclosing_end = not end
        return self

    def name(self, name:str) -> Username:
        self._name = name
        return self

    def adjective(self, adjective:str) -> Username:
        self._adjective = adjective
        return self

    def str_generator(self):
        if self._enclosing_start:
            yield self._enclosing

        if self._adjective:
            yield self._adjective

        yield self._name

        if self._enclosing_end:
            yield self._enclosing[::-1]

        if self._numerical_end_enabled:
            yield self._numerical_end


    def __str__(self) -> str:
        return "".join(self.str_generator())